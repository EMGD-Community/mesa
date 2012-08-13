/**************************************************************************
 * 
 * Copyright 2007 Tungsten Graphics, Inc., Cedar Park, Texas.
 * All Rights Reserved.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a
 * copy of this software and associated documentation files (the
 * "Software"), to deal in the Software without restriction, including
 * without limitation the rights to use, copy, modify, merge, publish,
 * distribute, sub license, and/or sell copies of the Software, and to
 * permit persons to whom the Software is furnished to do so, subject to
 * the following conditions:
 * 
 * The above copyright notice and this permission notice (including the
 * next paragraph) shall be included in all copies or substantial portions
 * of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
 * OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
 * IN NO EVENT SHALL TUNGSTEN GRAPHICS AND/OR ITS SUPPLIERS BE LIABLE FOR
 * ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
 * TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
 * SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 * 
 **************************************************************************/

/* Authors:
 *  Brian Paul
 */

#include "util/u_inlines.h"
#include "util/u_memory.h"

#include "draw/draw_context.h"

#include "lp_context.h"
#include "lp_screen.h"
#include "lp_state.h"
#include "lp_debug.h"
#include "state_tracker/sw_winsys.h"


static void *
llvmpipe_create_sampler_state(struct pipe_context *pipe,
                              const struct pipe_sampler_state *sampler)
{
   struct pipe_sampler_state *state = mem_dup(sampler, sizeof *sampler);

   if (LP_PERF & PERF_NO_MIP_LINEAR) {
      if (state->min_mip_filter == PIPE_TEX_MIPFILTER_LINEAR)
	 state->min_mip_filter = PIPE_TEX_MIPFILTER_NEAREST;
   }

   if (LP_PERF & PERF_NO_MIPMAPS)
      state->min_mip_filter = PIPE_TEX_MIPFILTER_NONE;

   if (LP_PERF & PERF_NO_LINEAR) {
      state->mag_img_filter = PIPE_TEX_FILTER_NEAREST;
      state->min_img_filter = PIPE_TEX_FILTER_NEAREST;
   }

   return state;
}


static void
llvmpipe_bind_sampler_states(struct pipe_context *pipe,
                             unsigned shader,
                             unsigned num, void **samplers)
{
   struct llvmpipe_context *llvmpipe = llvmpipe_context(pipe);
   unsigned i;

   assert(num <= PIPE_MAX_SAMPLERS);

   /* Check for no-op */
   if (num == llvmpipe->num_samplers[shader] &&
       !memcmp(llvmpipe->samplers[shader], samplers, num * sizeof(void *)))
      return;

   draw_flush(llvmpipe->draw);

   for (i = 0; i < num; ++i)
      llvmpipe->samplers[shader][i] = samplers[i];
   for (i = num; i < PIPE_MAX_SAMPLERS; ++i)
      llvmpipe->samplers[shader][i] = NULL;

   llvmpipe->num_samplers[shader] = num;

   /* XXX call draw_set_samplers() here for geometry shaders once
    * draw_set_samplers() is extended to accept a shader argument.
    */
   if (shader == PIPE_SHADER_VERTEX) {
      draw_set_samplers(llvmpipe->draw,
                        llvmpipe->samplers[PIPE_SHADER_VERTEX],
                        llvmpipe->num_samplers[PIPE_SHADER_VERTEX]);
   }

   llvmpipe->dirty |= LP_NEW_SAMPLER;
}


static void
llvmpipe_bind_fragment_sampler_states(struct pipe_context *pipe,
                                      unsigned num, void **samplers)
{
   llvmpipe_bind_sampler_states(pipe, PIPE_SHADER_FRAGMENT, num, samplers);
}


static void
llvmpipe_bind_vertex_sampler_states(struct pipe_context *pipe,
                                    unsigned num, void **samplers)
{
   llvmpipe_bind_sampler_states(pipe, PIPE_SHADER_VERTEX, num, samplers);
}


static void
llvmpipe_bind_geometry_sampler_states(struct pipe_context *pipe,
                                      unsigned num, void **samplers)
{
   llvmpipe_bind_sampler_states(pipe, PIPE_SHADER_GEOMETRY, num, samplers);
}

static void
llvmpipe_set_sampler_views(struct pipe_context *pipe,
                           unsigned shader,
                           unsigned num,
                           struct pipe_sampler_view **views)
{
   struct llvmpipe_context *llvmpipe = llvmpipe_context(pipe);
   uint i;

   assert(num <= PIPE_MAX_SAMPLERS);

   /* Check for no-op */
   if (num == llvmpipe->num_sampler_views[shader] &&
       !memcmp(llvmpipe->sampler_views[shader], views, num * sizeof(struct pipe_sampler_view *)))
      return;

   draw_flush(llvmpipe->draw);

   for (i = 0; i < PIPE_MAX_SAMPLERS; i++) {
      struct pipe_sampler_view *view = i < num ? views[i] : NULL;

      pipe_sampler_view_reference(&llvmpipe->sampler_views[shader][i], view);
   }

   llvmpipe->num_sampler_views[shader] = num;

   /* XXX call draw_set_sampler_views() here for geometry shaders once
    * draw_set_sampler_views() is extended to accept a shader argument.
    */
   if (shader == PIPE_SHADER_VERTEX) {
      draw_set_sampler_views(llvmpipe->draw,
                             llvmpipe->sampler_views[PIPE_SHADER_VERTEX],
                             llvmpipe->num_sampler_views[PIPE_SHADER_VERTEX]);
   }

   llvmpipe->dirty |= LP_NEW_SAMPLER_VIEW;
}


static void
llvmpipe_set_fragment_sampler_views(struct pipe_context *pipe,
                                    unsigned num,
                                    struct pipe_sampler_view **views)
{
   llvmpipe_set_sampler_views(pipe, PIPE_SHADER_FRAGMENT, num, views);
}


static void
llvmpipe_set_vertex_sampler_views(struct pipe_context *pipe,
                                  unsigned num,
                                  struct pipe_sampler_view **views)
{
   llvmpipe_set_sampler_views(pipe, PIPE_SHADER_VERTEX, num, views);
}


static void
llvmpipe_set_geometry_sampler_views(struct pipe_context *pipe,
                                    unsigned num,
                                    struct pipe_sampler_view **views)
{
   llvmpipe_set_sampler_views(pipe, PIPE_SHADER_GEOMETRY, num, views);
}

static struct pipe_sampler_view *
llvmpipe_create_sampler_view(struct pipe_context *pipe,
                            struct pipe_resource *texture,
                            const struct pipe_sampler_view *templ)
{
   struct pipe_sampler_view *view = CALLOC_STRUCT(pipe_sampler_view);

   if (view) {
      *view = *templ;
      view->reference.count = 1;
      view->texture = NULL;
      pipe_resource_reference(&view->texture, texture);
      view->context = pipe;
   }

   return view;
}


static void
llvmpipe_sampler_view_destroy(struct pipe_context *pipe,
                              struct pipe_sampler_view *view)
{
   pipe_resource_reference(&view->texture, NULL);
   FREE(view);
}


static void
llvmpipe_delete_sampler_state(struct pipe_context *pipe,
                              void *sampler)
{
   FREE( sampler );
}


/**
 * Called during state validation when LP_NEW_SAMPLER_VIEW is set.
 */
void
llvmpipe_prepare_vertex_sampling(struct llvmpipe_context *lp,
                                 unsigned num,
                                 struct pipe_sampler_view **views)
{
   unsigned i;
   uint32_t row_stride[PIPE_MAX_TEXTURE_LEVELS];
   uint32_t img_stride[PIPE_MAX_TEXTURE_LEVELS];
   const void *data[PIPE_MAX_TEXTURE_LEVELS];

   assert(num <= PIPE_MAX_VERTEX_SAMPLERS);
   if (!num)
      return;

   for (i = 0; i < PIPE_MAX_VERTEX_SAMPLERS; i++) {
      struct pipe_sampler_view *view = i < num ? views[i] : NULL;

      if (view) {
         struct pipe_resource *tex = view->texture;
         struct llvmpipe_resource *lp_tex = llvmpipe_resource(tex);

         /* We're referencing the texture's internal data, so save a
          * reference to it.
          */
         pipe_resource_reference(&lp->mapped_vs_tex[i], tex);

         if (!lp_tex->dt) {
            /* regular texture - setup array of mipmap level pointers */
            int j;
            for (j = view->u.tex.first_level; j <= tex->last_level; j++) {
               data[j] =
                  llvmpipe_get_texture_image_all(lp_tex, j, LP_TEX_USAGE_READ,
                                                 LP_TEX_LAYOUT_LINEAR);
               row_stride[j] = lp_tex->row_stride[j];
               img_stride[j] = lp_tex->img_stride[j];
            }
         }
         else {
            /* display target texture/surface */
            /*
             * XXX: Where should this be unmapped?
             */
            struct llvmpipe_screen *screen = llvmpipe_screen(tex->screen);
            struct sw_winsys *winsys = screen->winsys;
            data[0] = winsys->displaytarget_map(winsys, lp_tex->dt,
                                                PIPE_TRANSFER_READ);
            row_stride[0] = lp_tex->row_stride[0];
            img_stride[0] = lp_tex->img_stride[0];
            assert(data[0]);
         }
         draw_set_mapped_texture(lp->draw,
                                 i,
                                 tex->width0, tex->height0, tex->depth0,
                                 view->u.tex.first_level, tex->last_level,
                                 row_stride, img_stride, data);
      }
   }
}

void
llvmpipe_cleanup_vertex_sampling(struct llvmpipe_context *ctx)
{
   unsigned i;
   for (i = 0; i < Elements(ctx->mapped_vs_tex); i++) {
      pipe_resource_reference(&ctx->mapped_vs_tex[i], NULL);
   }
}

void
llvmpipe_init_sampler_funcs(struct llvmpipe_context *llvmpipe)
{
   llvmpipe->pipe.create_sampler_state = llvmpipe_create_sampler_state;

   llvmpipe->pipe.bind_fragment_sampler_states  = llvmpipe_bind_fragment_sampler_states;
   llvmpipe->pipe.bind_vertex_sampler_states  = llvmpipe_bind_vertex_sampler_states;
   llvmpipe->pipe.bind_geometry_sampler_states  = llvmpipe_bind_geometry_sampler_states;
   llvmpipe->pipe.set_fragment_sampler_views = llvmpipe_set_fragment_sampler_views;
   llvmpipe->pipe.set_vertex_sampler_views = llvmpipe_set_vertex_sampler_views;
   llvmpipe->pipe.set_geometry_sampler_views = llvmpipe_set_geometry_sampler_views;
   llvmpipe->pipe.create_sampler_view = llvmpipe_create_sampler_view;
   llvmpipe->pipe.sampler_view_destroy = llvmpipe_sampler_view_destroy;
   llvmpipe->pipe.delete_sampler_state = llvmpipe_delete_sampler_state;
}
