Name:       mesa
Summary:    Mesa graphics libraries
Version:    8.1.0+1+5f3f6
Release:    1 
Group:      System/Libraries
License:    MIT
URL:        http://www.mesa3d.org/beta
Source0:    %{name}-%{version}.tar.bz2
Source1:    mesa-rpmlintrc
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(dri2proto)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig autoconf automake
BuildRequires:  libxml2-python
BuildRequires:  llvm-devel
BuildRequires:  expat-devel
BuildRequires:  python-devel
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  makedepend

%description
Mesa is an open-source implementation of the OpenGL specification  -
a system for rendering interactive 3D graphics.

%package dri-drivers-devel
Summary:    Mesa-based DRI development files
Group:      Development/Libraries

%description dri-drivers-devel
Mesa-based DRI driver development files.

%ifarch %ix86
%package dri-i965-driver
Summary:    Mesa-based DRI drivers
Group:      System/X Hardware Support
Provides:   mesa-dri-drivers = %{version}-%{release}

%description dri-i965-driver
Mesa-based i965 DRI driver.

%package dri-i915-driver
Summary:    Mesa-based DRI drivers
Group:      System/X Hardware Support
Provides:   mesa-dri-drivers = %{version}-%{release}

%description dri-i915-driver
Mesa-based i915 DRI driver.
%endif

%package dri-swrast-driver
Summary:    Mesa-based DRI drivers
Group:      System/X Hardware Support
Provides:   mesa-dri-drivers = %{version}-%{release}

%description dri-swrast-driver
Mesa-based swrast DRI driver.

%package libGL
Summary:    Mesa libGL runtime libraries and DRI drivers
Group:      System/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libGL = %{version}-%{release}

%description libGL
Mesa libGL runtime library.

%package libGLESv2
Summary:    Mesa libGLESv2 runtime libraries
Group:      System/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libGLESv2 = %{version}-%{release}

%description libGLESv2
Mesa libGLESv2 runtime library.

%package libGLESv1
Summary:    Mesa libGLESv1 runtime libraries
Group:      System/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libGLESv1 = %{version}-%{release}

%description libGLESv1
Mesa libGLESv1 runtime library.


%package libGLESv2-compat
Summary:    Mesa libGLESv2 runtime compatibility library
Group:      System/Libraries
Requires:   libGLESv2.so.2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
#Provides:   libGLESv2.so

%description libGLESv2-compat
Mesa libGLESv2 runtime compatibility library.

%package libgbm
Summary:    Mesa General Buffer Management library
Group:      System/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libgbm = %{version}-%{release}

%description libgbm
Mesa General Buffer Management library

%package libgbm-devel
Summary:    Mesa libgbm development package
Group:      Development/Libraries
Requires:   mesa-libgbm = %{version}-%{release}
Provides:   libgbm-devel

%description libgbm-devel
Mesa libgbm library development package

%package libwayland-egl
Summary:    Wayland EGL library
Group:      System/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libwayland-egl = %{version}-%{release}

%description libwayland-egl
Wayland EGL library

%package libwayland-egl-devel
Summary:    Mesa libwayland-egl development package
Group:      Development/Libraries
Requires:   libwayland-egl = %{version}-%{release}
Provides:   libwayland-egl-devel

%description libwayland-egl-devel
Mesa libwayland-egl library development package

%package libEGL
Summary:    Mesa libEGL runtime libraries and DRI drivers
Group:      System/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides:   libEGL = %{version}-%{release}

%description libEGL
Mesa libEGL runtime library.

%package libEGL-compat
Summary:    Mesa libEGL runtime compatibility library
Group:      System/Libraries
Requires:   libEGL.so.1
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
#Provides:   libEGL.so

%description libEGL-compat
Mesa libEGL runtime compatibility library.

%package libGLU
Summary:    Mesa libGLU runtime library
Group:      System/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description libGLU
Mesa OpenGL library Utility runtime library

%package libGL-devel
Summary:    Mesa libGL development package
Group:      Development/Libraries
Requires:   mesa-libGL = %{version}-%{release}
Requires:   libx11-devel
Provides:   libGL-devel

%description libGL-devel
Mesa OpenGL library development package

%package libGLESv2-devel
Summary:    Mesa libGLESv2 development package
Group:      Development/Libraries
Requires:   mesa-libGLESv2 = %{version}-%{release}
Provides:   libGLESv2-devel
Obsoletes:   mesa-libGLESv2-compat

%description libGLESv2-devel
Mesa OpenGLESv2 library development package

%package libGLESv1-devel
Summary:    Mesa libGLESv1 development package
Group:      Development/Libraries
Requires:   mesa-libGLESv1 = %{version}-%{release}
Provides:   libGLESv1-devel
Obsoletes:   mesa-libGLESv1-compat

%description libGLESv1-devel

Mesa OpenGLES
%package libEGL-devel
Summary:    Mesa libEGL development package
Group:      Development/Libraries
Requires:   mesa-libEGL = %{version}-%{release}
Provides:   libEGL-devel
Obsoletes:   mesa-libEGL-compat

%description libEGL-devel
Mesa EGL library development package

%package libGLU-devel
Summary:    Mesa libGLU development package
Group:      Development/Libraries
Requires:   mesa-libGLU = %{version}-%{release}
Requires:   libGL-devel
Provides:   libGLU-devel

%description libGLU-devel
Mesa OpenGL library Utility development package

%prep
%setup -q -n MesaLib-%{version} -b1

%build

%reconfigure \
    --disable-gallium-egl \
    --enable-gles1 \
    --enable-gles2 \
    --with-egl-platforms=wayland,drm \
    --enable-gbm \
    --enable-gallium-gbm \
    --enable-shared-glapi \
    --with-dri-drivers=swrast,i915,i965
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install



%post libGL -p /sbin/ldconfig

%postun libGL -p /sbin/ldconfig


%post libGLESv2 -p /sbin/ldconfig

%postun libGLESv2 -p /sbin/ldconfig


%post libGLESv2-compat -p /sbin/ldconfig

%postun libGLESv2-compat -p /sbin/ldconfig


%post libEGL -p /sbin/ldconfig

%postun libEGL -p /sbin/ldconfig

%post libwayland-egl -p /sbin/ldconfig

%postun libwayland-egl -p /sbin/ldconfig

%post libEGL-compat -p /sbin/ldconfig

%postun libEGL-compat -p /sbin/ldconfig


%post libGLU -p /sbin/ldconfig

%postun libGLU -p /sbin/ldconfig

%ifarch %ix86
%files dri-drivers-devel
%defattr(-,root,root,-)
%{_libdir}/pkgconfig/dri.pc
/usr/lib/dri/r300_dri.so
/usr/lib/dri/r600_dri.so
/usr/lib/dri/vmwgfx_dri.so

%files dri-i965-driver
%defattr(-,root,root,-)
%{_libdir}/dri/i965_dri.so

%files dri-i915-driver
%defattr(-,root,root,-)
%{_libdir}/dri/i915_dri.so

%files dri-swrast-driver
%defattr(-,root,root,-)
%{_libdir}/dri/swrast_dri.so
%endif

%files libGL
%defattr(-,root,root,-)
%{_libdir}/libGL.so.*
%{_libdir}/libglapi.so.*

%files libGLESv2
%defattr(-,root,root,-)
%{_libdir}/libGLESv2.so.*

%files libGLESv1
%defattr(-,root,root,-)
%{_libdir}/libGLESv1_CM.so.*


%files libGLESv2-compat
%defattr(-,root,root,-)
%{_libdir}/libGLESv2.so

%files libgbm
%defattr(-,root,root,-)
%{_libdir}/libgbm.so.*
%{_libdir}/gbm/*
/etc/drirc
%{_libdir}/dri/libdricore.so
%{_libdir}/dri/libglsl.so

%files libgbm-devel
%defattr(-,root,root,-)
%{_includedir}/gbm.h
%{_libdir}/libgbm.so
%{_libdir}/pkgconfig/gbm.pc

%files libwayland-egl
%defattr(-,root,root,-)
%{_libdir}/libwayland-egl.so.*

%files libwayland-egl-devel
%defattr(-,root,root,-)
%{_libdir}/libwayland-egl.so
%{_libdir}/pkgconfig/wayland-egl.pc

%files libEGL
%defattr(-,root,root,-)
%{_libdir}/libEGL.so.*

%files libEGL-compat
%defattr(-,root,root,-)
%{_libdir}/libEGL.so

%files libGLU
%defattr(-,root,root,-)
%{_libdir}/libGLU.so.*

%files libGL-devel
%defattr(-,root,root,-)
%{_includedir}/GL/gl.h
%{_includedir}/GL/gl_mangle.h
%{_includedir}/GL/glext.h
%{_includedir}/GL/glx.h
%{_includedir}/GL/glx_mangle.h
%{_includedir}/GL/glxext.h
%{_includedir}/GL/osmesa.h
%{_includedir}/GL/vms_x_fix.h
%{_includedir}/GL/wglext.h
%{_includedir}/GL/wmesa.h
%{_libdir}/libglapi.so

%ifarch %ix86
%dir %{_includedir}/GL/internal
%{_includedir}/GL/internal/dri_interface.h
%endif
%{_libdir}/libGL.so
%{_libdir}/pkgconfig/gl.pc

%files libGLESv2-devel
%defattr(-,root,root,-)
%{_libdir}/libGLESv2.so
%{_includedir}/GLES2/gl2.h
%{_includedir}/GLES2/gl2ext.h
%{_includedir}/GLES2/gl2platform.h
%{_libdir}/pkgconfig/glesv2.pc


%files libGLESv1-devel
%defattr(-,root,root-)
%{_libdir}/libGLESv1_CM.so
%{_includedir}/GLES/egl.h
%{_includedir}/GLES/gl.h
%{_includedir}/GLES/glext.h
%{_includedir}/GLES/glplatform.h
%{_libdir}/pkgconfig/glesv1_cm.pc


%files libEGL-devel
%defattr(-,root,root,-)
%{_libdir}/libEGL.so
%dir %{_includedir}/EGL
%{_includedir}/EGL/egl.h
%{_includedir}/EGL/eglext.h
%{_includedir}/EGL/eglplatform.h
%{_includedir}/EGL/eglmesaext.h
%dir %{_includedir}/KHR
%{_includedir}/KHR/khrplatform.h
%{_libdir}/pkgconfig/egl.pc

%files libGLU-devel
%defattr(-,root,root,-)
%{_libdir}/libGLU.so
%{_libdir}/pkgconfig/glu.pc
%{_includedir}/GL/glu.h
%{_includedir}/GL/glu_mangle.h

%changelog
* Mon Apr 26 2012 Xinyun Liu<xinyun.liu@intel.com> - 8.0.1
- Add GLESv1 package
* Mon Mar 19 2012 Rusty Lynch <rusty.lynch@intel.com> - 8.0.1
- mesa 8.0.1
* Tue May  3 2011 Li Peng <peng.li@intel.com> - 7.10.2
- mesa 7.10.2
* Mon Apr 18 2011 Li Peng <peng.li@intel.com> - 7.9.1
- Fix BMC #13274: mcompositor (Mesa, EGL) crashes on unchecked pointer
* Tue Mar 29 2011 Feng Haitao <haitao.feng@intel.com> - 7.9.1
- Fix a typo in EGL software driver. BMC #14979
* Fri Mar 25 2011 Feng Haitao <haitao.feng@intel.com> - 7.9.1
- Enable surfaceless for EGL software driver. BMC #14850
* Thu Feb 17 2011 Li Peng <peng.li@intel.com> - 7.9.1
- Fix BMC #13591 (add dri2 release texture image method)
* Thu Feb 10 2011 Li Peng <peng.li@intel.com> - 7.9.1
- Fix BMC #13005 (Graphics GLSL issue lead to camera preview fail on
  Pinetrail)
* Tue Jan 25 2011 Feng Haitao <haitao.feng@intel.com> - 7.9.1
- Enable an EGL driver to work with swrast dri2 driver. BMC #12819
* Mon Jan 24 2011 Fathi Boudra <fathi.boudra@nokia.com> - 7.9.1
- Add Requires libX11-devel to mesa-libGL-devel (BMC#12001)
- Revert: make mesa-libGLUT/mesa-libGLUT-devel obsolete freeglut/freeglut-devel
  (BMC#12744)
* Tue Jan 18 2011 Li Peng <peng.li@intel.com> - 7.9.1
- update to mesa 7.9.1, a bugfix release. BMC #12545
* Mon Oct 25 2010 Li Peng <peng.li@intel.com> - 7.9
- Fix BMC #5962 (netbook duihome failure on GLESv2 enabled Qt)
* Fri Oct  8 2010 Li Peng <peng.li@intel.com> - 7.9
- update to mesa 7.9 final release
* Wed Sep 29 2010 Li Peng <peng.li@intel.com> - 7.9~rc2~git5d3a4317e8
- update to mesa 7.9-rc2
* Fri Sep 17 2010 Liu Xinyun <xinyun.liu@intel.com> - 7.8.99.1~gitb018ea19a3
- Add osmesa.pc for devel package. Fix BMC #6854.
* Wed Sep  8 2010 Li Peng <peng.li@intel.com> - 7.8.99.1~gitb018ea19a3
- handset driver reuse the devel packages of EGL, OpenVG and GLES,
  remove devel package dependency on mesa lib package.
* Mon Sep  6 2010 Li Peng <peng.li@intel.com> - 7.8.99.1~gitb018ea19a3
- Add new package mesa-libOSMesa
- Remove unnecessary dependency of mesa-dri-drivers
* Thu Aug 26 2010 Li Peng <peng.li@intel.com> - 7.8.99.1~gitb018ea19a3
- Now mesa-dri-drivers isn't a must requirement for mesa-libGL
* Wed Aug 25 2010 Li Peng <peng.li@intel.com> - 7.8.99.1~gitb018ea19a3
- Add new package mesa-libOpenVG
* Tue Aug 24 2010 Li Peng <peng.li@intel.com> - 7.8.99~gitda7bd6a90e
- update to latest mesa git
- update Provides and Requires of libGLESv2-compat and libEGL-compat
* Mon Aug  2 2010 Li Peng <peng.li@intel.com> - 7.8.99~gitda7bd6a90e
- Add mesa-libGLESv2-compat and mesa-libEGL-compat package to
  support application compatibility for MeeGo and Harmattan on ARM
* Thu Jul 29 2010 Li Peng <peng.li@intel.com> - 7.8.99~gitda7bd6a90e
- make mesa-libGLUT and mesa-libGLUT-devel obsolete freeglut and freeglut-devel
* Tue Jun 29 2010 Li Peng <peng.li@intel.com> - 7.8.99~gitda7bd6a90e
- mesa 7.8.99~gitda7bd6a90e
* Tue Jun 22 2010 Li Peng <peng.li@intel.com> - 7.8.2
- mesa 7.8.2
* Thu May 13 2010 Priya Vijayan <priya.vijayan@intel.com> - 7.8.1
- Add pbuffer patches through spectacle instead of directly adding to spec
* Wed Apr 28 2010 Prajwal Mohan <prajwal.karur.mohan@intel.com> - 7.8.1
- Added Mesa workaround to report PBUFFER configs - Fix #352
* Wed Apr 28 2010 Li Peng <peng.li@intel.com> - 7.8.1
- Add glut package per handset requirement
* Thu Apr 15 2010 Li Peng <peng.li@intel.com> - 7.8.1
- don't package egl_glx.so, which is broken
- add package egl-utils for egl demos and utilities
* Wed Apr 14 2010 Li Peng <peng.li@intel.com> - 7.8.1
- fix DRI2 event type
* Fri Apr  9 2010 Li Peng <peng.li@intel.com> - 7.8.1
- fix MeeGo bug #34 (gnome-control-center crash on Calpella)
* Tue Apr  6 2010 Li Peng <peng.li@intel.com> - 7.8.1
- Mesa 7.8.1
* Wed Mar 31 2010 Li Peng <peng.li@intel.com> - 7.8
- Mesa 7.8
* Tue Mar 30 2010 Li Peng <peng.li@intel.com> - 7.7.99.902~git094c6fbc45
- revoke the screen flicker fix, it break gfx perf test
  and cause critical bugs.
* Fri Mar 26 2010 Li Peng <peng.li@intel.com> - 7.7.99.902~git094c6fbc45
- fix screen flicker issue at full screen flipping
* Wed Mar 24 2010 Anas Nashif <anas.nashif@intel.com> - 7.7.99.902~git094c6fbc45
- Fixed summary
* Wed Mar 24 2010 Li Peng <peng.li@intel.com> 7.7.99.902
- enable egl option for handset requirement
* Tue Mar 23 2010 Li Peng <peng.li@intel.com> 7.7.99.902
- update to mesa 7.8-rc2
* Thu Mar 18 2010 Li Peng <peng.li@intel.com> 7.7.99.901
- apply fixes for texture-tiling from mesa git master
- fixes group info in spec
* Mon Mar 15 2010 Li Peng <peng.li@intel.com> 7.7.99.901
- update to lastest mesa-7.8 branch, git commit 346298c765
  disable texture-tiling for now.
* Mon Mar  1 2010 Li Peng <peng.li@intel.com> 7.7.99
- disable "GL_ARB_texture_rectangle" extension for i915
* Tue Feb  9 2010 Li Peng <peng.li@intel.com> 7.7.99
- upgrade to latest mesa
* Wed Dec 23 2009 Li Peng <peng.li@intel.com> 7.7
- Mesa 7.7
* Fri Oct 16 2009 Li Peng <peng.li@intel.com> 7.6
- Fix MB #6803 (Videos in Swedish locale have an incorrect colour)
* Fri Oct  9 2009 Li Peng <peng.li@intel.com> 7.6
- Mesa 7.6
* Wed Jul  1 2009 Li Peng <peng.li@intel.com> 7.5
- Fix #3648
* Mon Jun 29 2009 Li Peng <peng.li@intel.com> 7.5
- Mesa 7.5-rc4
* Tue Jun 23 2009 Li Peng <peng.li@intel.com> 7.5
- intel gfx 2009Q2-rc2 release
* Wed May 27 2009 Li Peng <peng.li@intel.com> 7.4.2
- Mesa 7.4.2
* Mon Apr 27 2009 Li Peng <peng.li@intel.com> 7.4.1
- Update to Mesa 7.4.1, a bugfix release
* Fri Apr  3 2009 Peng Li <peng.li@intel.com> 7.4
- Upgrade to Mesa 7.4
* Thu Feb 26 2009 Peng Li <peng.li@intel.com> 7.2
- add patch to fix for the memory allocation
- add patch to support G33-like new graphic chip
* Tue Jan 27 2009 Li Peng <peng.li@intel.com> 7.2
- Remove DRI2 fix patch to sync with upstream
* Mon Jan 26 2009 Anas Nashif <anas.nashif@intel.com> 7.2
- Fix performance issues with DRI2
* Fri Jan 16 2009 Peng Li <peng.li@intel.com> 7.2
- update to 2008Q4 stable release 'mesa-20090115.tar.gz' at
  http://intellinuxgraphics.org/2008Q4.html
* Tue Jan 13 2009 Peng Li <peng.li@intel.com> 7.2
- update to latest 2008Q4 pre-release 'mesa-20090112.tar.gz' at
  http://intellinuxgraphics.org/download.html
* Mon Dec 22 2008 Peng Li <peng.li@intel.com> 7.2
- update to 2008Q4 pre-release at
  http://intellinuxgraphics.org/download.html
* Sat Dec 20 2008 Arjan van de Ven <arjan@linux.intel.com> 7.1
- Fix misisng buildrequires:
* Tue Dec 16 2008 Anas Nashif <anas.nashif@intel.com> 7.1
- Fixed rpmlint errors in Summary tag
* Thu Dec  4 2008 Peng Li <peng.li@intel.com> 7.1
- change source to intel-2008-q3 branch, commit
  8f8892525a560b0e68780d58a1e127b304a31e8b
* Sat Oct  4 2008 Anas Nashif <anas.nashif@intel.com> 7.1
- split package into multiple drivers
* Thu Sep 25 2008 Peng Li <peng.li@intel.com> 7.1
- package upgrade for dri2
* Tue Sep 23 2008 Peng Li <peng.li@intel.com> 7.1
- cleanup rpm spec, remove osmesa, demo and man package
* Fri Sep  5 2008 Peng Li <peng.li@intel.com> 7.1
- remove dependency on makedepend
* Wed Aug 13 2008 Peng Li <peng.li@intel.com>
- add swrast in dri driver build, which is needed to boot X in VM
* Fri Jun 27 2008 Adam Jackson <ajax@redhat.com> 7.1-0.37
- Drop mesa-source subpackage.  Man that feels good.
* Fri Jun 27 2008 Adam Jackson <ajax@redhat.com> 7.1-0.36
- Today's snapshot.
- Package swrast_dri for the new X world order.
- Split DRI drivers to their own subpackage.
* Thu Jun 12 2008 Dave Airlie <airlied@redhat.com> 7.1-0.35
- Update mesa to latest git snapshot - drop patches merged upstream
* Wed Jun  4 2008 Adam Jackson <ajax@redhat.com> 7.1-0.34
- Link libdricore with gcc instead of ld, so we automagically pick up the
  ld --build-id flags.
* Wed May 28 2008 Dave Airlie <airlied@redhat.com> 7.1-0.33
- Add initial r500 3D driver
* Tue May 13 2008 Adam Jackson <ajax@redhat.com> 7.1-0.32
- Update dri2proto requirement.  (#446166)
* Sat May 10 2008 Dave Airlie <airlied@redhat.com> 7.1-0.31
- Bring in a bunch of fixes from upstream, missing rs690 pci id,
- DRI2 + modeset + 965 + compiz + alt-tab fixed.
* Wed May  7 2008 Dave Airlie <airlied@redhat.com> 7.1-0.30
- fix googleearth on Intel 965 (#443930)
- disable classic warning to avoid people reporting it.
* Mon May  5 2008 Dave Airlie <airlied@redhat.com> 7.1-0.29
- mesa-7.1-f9-intel-and-radeon-fixes.patch - Update mesa
  package with cherrypicked fixes from master.
- Fixes numerous i965 3D issues
- Fixes compiz on rs48x and rs690 radeon chipsets
* Fri Apr 18 2008 Dave Airlie <airlied@redhat.com> 7.1-0.28
- okay fire me now - I swear it runs compiz really well...
- fix more bugs on 965
* Fri Apr 18 2008 Dave Airlie <airlied@redhat.com> 7.1-0.27
- why yes, that is a brown paper bag
- fix glxgears on 965
* Fri Apr 18 2008 Dave Airlie <airlied@redhat.com> 7.1-0.26
- fix compiz alt-tab crashing on out of the box intel driver
- some other upstream bugfixes as well
* Tue Apr 15 2008 Dave Airlie <airlied@redhat.com> 7.1-0.25
- Rebase to latest upstream - drop patches applied there.
* Sat Apr 12 2008 Dennis Gilmore <dennis@ausil.us> 7.1-0.24
- add patch so that we only build dri drivers on sparc that are remotely
  useful.  sis driver breaks the build and the intel ones will never exist
* Thu Apr 10 2008 Adam Jackson <ajax@redhat.com> 7.1-0.23
- mesa-7.1-link-shared.patch: Make a libdricore.so from libmesa.a, install
  it into %%%%_libdir/dri, and link the DRI drivers against it.  Drops ~20M
  from the installed system (not including debuginfo).  Inspired by a
  similar patch in openSUSE but reworked to be compatible with the OSMesa
  build.
* Wed Apr  9 2008 Adam Jackson <ajax@redhat.com> 7.1-0.22
- mesa-7.1-visual-crash.patch: Fix a segfault if DRI unavailable.
- mesa-7.1-fbconfig-fix.patch: Fix fbconfig comparisons.
- mesa-7.1-dri2.patch: Fix a header path.
- Add buildreqs for the demos that suddenly stopped compiling.
* Mon Mar 31 2008 Kristian Høgsberg <krh@redhat.com> - 7.1-0.21
- Update git snapshot to pull in DRI2 direct rendering.
- Add conflicts for xservers that don't understand the new DRI driver
  interface.
* Tue Mar 11 2008 Kristian Høgsberg <krh@redhat.com> - 7.1-0.20
- Looks like the TexOffset extension does not work, disable for now.
- Bump to 20080311 snapshot to get DRI2 tfp fixes.
* Mon Mar  3 2008 Kristian Høgsberg <krh@redhat.com> - 7.1-0.19
- Bump to latest git snapshot.
- Drop mesa-7.1-dri-drivers.patch, it's upstream.
- Require libdrm-devel >= 2.4.0-0.5
* Mon Mar  3 2008 Dave Airlie <airlied@redhat.com> 7.1-0.18
- fix i915 build due to symbol visibility
* Tue Feb 26 2008 Adam Jackson <ajax@redhat.com> 7.1-0.17
- Fix OSMesa symlink bug. (#424545)
- Build OSMesa with -Os to be slightly less bloaty.
- Re-add osmesa.h to libOSMesa-devel.
- Really restore -fvisibility=hidden.
* Thu Feb 21 2008 Adam Jackson <ajax@redhat.com> 7.1-0.16
- Fix build on powerpc and amd64.
- Disable %%%%_smp_mflags for DRI drivers for now.
* Mon Feb 18 2008 Adam Jackson <ajax@redhat.com> 7.1-0.15
- Today's git snapshot, additional headers for DRI2 love.
* Fri Feb 15 2008 Adam Jackson <ajax@redhat.com> 7.1-0.14
- Fix build on lib64 machines.
* Fri Feb 15 2008 Adam Jackson <ajax@redhat.com> 7.1-0.13
- Restore -fvisibility=hidden.
- Fix autotooling.
* Fri Feb 15 2008 Adam Jackson <ajax@redhat.com> 7.1-0.12
- Fix file conflict with bsd-games on /usr/bin/rain.
* Fri Feb 15 2008 Adam Jackson <ajax@redhat.com> 7.1-0.11
- Today's git snapshot.
- Massive spec overhaul to use new buildsystem.
* Tue Feb 12 2008 Adam Jackson <ajax@redhat.com> 7.1-0.10
- mesa-7.1-sis-ia64.patch: Fix sis driver on ia64. (#432428)
* Mon Feb 11 2008 Adam Jackson <ajax@redhat.com> 7.1-0.9
- mesa-7.1-ia64-build-fix.patch: Fix build on ia64. (#427558)
* Tue Jan 22 2008 Adam Jackson <ajax@redhat.com> 7.1-0.8
- Enable i915 DRI on E7221. (Carlos Martín, #425790)
* Mon Jan 21 2008 Adam Jackson <ajax@redhat.com>
- Make the demo seddery prettier.
* Tue Dec  4 2007 Dave Airlie <airlied@redhat.com> 7.1-0.7
- Remove references to libgl symbol from i915
* Fri Nov 30 2007 Dave Airlie <airlied@redhat.com> 7.1-0.6
- Rebuild against a new libdrm
* Tue Nov 27 2007 Adam Jackson <ajax@redhat.com> 7.1-0.5
- Rebase to today's git snapshot.
- Try even harder to not build or the Mesa glut.
* Thu Nov 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> 7.1-0.4
- link libOSMesa* against libselinux
* Mon Nov 12 2007 Adam Jackson <ajax@redhat.com> 7.1-0.3
- Drop xserver 1.1 source compatibility.
* Wed Nov  7 2007 Dave Airlie <airlied@redhat.com> 7.1-0.2
- fix DRI driver directory
* Thu Nov  1 2007 Adam Jackson <ajax@redhat.com> 7.1-0.1
- Fix EVR, 7.1pre > 7.1, that would have been bad.
- Fix %%%%setup to match.
* Thu Nov  1 2007 Dave Airlie <airlied@redhat.com> 7.1pre-0
- rebase Mesa to 7.1pre 74ced1e67f286a5e71e9877bc6844b2af5b9ab8d
* Thu Oct 18 2007 Dave Airlie <airlied@redhat.com> 7.0.1-7
- mesa-7.0.1-stable-branch.patch - Updated with more fixes from stable
- mesa-7.0.1-r300-fix-writemask.patch - fix r300 fragprog writemask
- mesa-7.0.1-r200-settexoffset.patch - add zero-copy TFP support for r200
* Fri Sep 28 2007 Dave Airlie <airlied@redhat.com> 7.0.1-6
- mesa-7.0.1-stable-branch.patch - Updated to close to 7.0.2-rc1
- This contains the fixes made to the upstream Mesa stable branch
  including fixes for 965 vblank interrupt issues along with a fix
  in the kernel - remove patches that already upstream.
- mesa-6.5.2-hush-synthetic-visual-warning.patch - dropped
- mesa-7.0-i-already-defined-glapi-you-twit.patch - dropped
- mesa-7.0.1-965-sampler-crash.patch - dropped
* Thu Sep  6 2007 Adam Jackson <ajax@redhat.com> 7.0.1-5
- mesa-7.0.1-965-sampler-crash.patch: Fix a crash with 965 in Torcs. (#262941)
* Tue Aug 28 2007 Adam Jackson <ajax@redhat.com> 7.0.1-4
- Rebuild for new libexpat.
* Wed Aug 15 2007 Dave Airlie <airlied@redhat.com> - 7.0.1-3
- mesa-7.0.1-stable-branch.patch - Add patches from stable branch
  includes support for some Intel chipsets
- mesa-7.0-use_master-r300.patch - Add r300 driver from master
* Tue Aug 14 2007 Dave Airlie <airlied@redhat.com> - 7.0.1-2
- missing build requires for Xfixes-devel and Xdamage-devel
* Mon Aug 13 2007 Dave Airlie <airlied@redhat.com> - 7.0.1-1
- Rebase to upstream 7.0.1 release
- ajax provided patches: for updated selinux awareness, build config
- gl visibility and picify were fixed upstream
- OS mesa library version are 6.5.3 not 7.0.1 - spec fix
* Wed Jul 25 2007 Jesse Keating <jkeating@redhat.com> - 6.5.2-16
- Rebuild for RH #249435
* Tue Jul 24 2007 Adam Jackson <ajax@redhat.com> 6.5.2-15
- Add dri_interface.h to mesa-libGL-devel, and conflict with
  xorg-x11-proto-devel versions that attempted to provide it.
* Tue Jul 10 2007 Adam Jackson <ajax@redhat.com> 6.5.2-14
- Add mesa-demos subpackage. (#247252)
* Mon Jul  9 2007 Adam Jackson <ajax@redhat.com> 6.5.2-13
- mesa-6.5.2-radeon-backports-231787.patch: One more fix for r300. (#231787)
* Mon Jul  9 2007 Adam Jackson <ajax@redhat.com> 6.5.2-12
- Don't install header files for APIs that we don't provide. (#247390)
* Fri Jul  6 2007 Adam Jackson <ajax@redhat.com> 6.5.2-11
- mesa-6.5.2-via-respect-my-cliplist.patch: Backport a via fix. (#247254)
* Tue Apr 10 2007 Adam Jackson <ajax@redhat.com> 6.5.2-10
- mesa-6.5.2-radeon-backports-231787.patch: Backport various radeon bugfixes
  from git. (#231787)
* Wed Apr  4 2007 Adam Jackson <ajax@redhat.com> 6.5.2-9
- mesa-6.5.2-bindcontext-paranoia.patch: Paper over a crash when doBindContext
  fails, to avoid, for example, crashing the server when using tdfx but
  without glide3 installed.
* Thu Mar  8 2007 Adam Jackson <ajax@redhat.com> 6.5.2-8
- Hush the (useless) warning about the synthetic visual not being supported.
* Fri Mar  2 2007 Adam Jackson <ajax@redhat.com> 6.5.2-7
- mesa-6.5.2-picify-dri-drivers.patch: Attempt to make the DRI drivers PIC.
- mesa-6.5.1-build-config.patch: Apply RPM_OPT_FLAGS to OSMesa too.
* Mon Feb 26 2007 Adam Jackson <ajax@redhat.com> 6.5.2-6
- mesa-6.5.2-libgl-visibility.patch: Fix non-exported GLX symbols (#229808)
- Require a sufficiently new libdrm at runtime too
- Make the arch macros do something sensible in the general case
* Tue Feb 20 2007 Adam Jackson <ajax@redhat.com> 6.5.2-5
- General spec cleanups
- Require current libdrm
- Build with -fvisibility=hidden
- Redo the way mesa-source is generated
- Add %%%%{?_smp_mflags} where appropriate
* Mon Dec 18 2006 Adam Jackson <ajax@redhat.com> 6.5.2-4
- Add i915tex and mach64 to the install set.
* Tue Dec 12 2006 Adam Jackson <ajax@redhat.com> 6.5.2-3
- mesa-6.5.2-xserver-1.1-source-compat.patch: Add some source-compatibility
  defines to dispatch.h so the X server will continue to build.
* Mon Dec  4 2006 Adam Jackson <ajax@redhat.com> 6.5.2-2.fc6
- Fix OSMesa file listing to use %%%%version for DSO number.  Note that this
  will still break on Mesa 7; oh well.
- Deleted file: directfbgl.h
* Sun Dec  3 2006 Kristian Høgsberg <krh@redhat.com> 6.5.2-1.fc6
- Update to 6.5.2.
* Mon Oct 16 2006 Kristian <krh@redhat.com> - 6.5.1-8.fc6
- Add i965-interleaved-arrays-fix.patch to fix (#209318).
* Sat Sep 30 2006 Soren Sandmann <sandmann@redhat.com> - 6.5.1-7.fc6
- Update to gl-manpages-1.0.1.tar.bz2 which doesn't use symlinks. (#184547)
* Sat Sep 30 2006 Soren Sandmann <sandmann@redhat.com> - 6.5.1-7.fc6
- Remove . after popd; add .gz in %%%%files section. (#184547)
* Sat Sep 30 2006 Soren Sandmann <sandmann@redhat.com>
- Use better tarball for gl man pages. (#184547)
* Fri Sep 29 2006 Kristian <krh@redhat.com> - 6.5.1-6.fc6
- Add -fno-strict-aliasing to compiler flags for i965 driver.
- Add post-6.5.1-i965-fixes.patch backport of i965 fixes from mesa CVS.
* Fri Sep 29 2006 Soren Sandmann <sandamnn@redhat.com> - 6.5.1-5.fc6
- Give the correct path for man page file lists.
* Thu Sep 28 2006 Soren Sandmann <sandmann@redhat.com> - 6.5.1-5.fc6
- Add GL man pages from X R6.9.  (#184547)
* Mon Sep 25 2006 Adam Jackson <ajackson@redhat.com> - 6.5.1-4.fc6
- mesa-6.5.1-build-config.patch: Add -lselinux to osmesa builds.  (#207767)
* Wed Sep 20 2006 Kristian Høgsberg <krh@redhat.com> - 6.5.1-3.fc6
- Bump xorg-x11-proto-devel BuildRequires to 7.1-8 so we pick up the
  latest GLX_EXT_texture_from_pixmap opcodes.
* Wed Sep 20 2006 Kristian Høgsberg <krh@redhat.com> - 6.5.1-2.fc6
- Remove mesa-6.5-drop-static-inline.patch.
* Tue Sep 19 2006 Kristian Høgsberg <krh@redhat.com> 6.5.1-1.fc6
- Bump to 6.5.1 final release.
- Drop libGLw subpackage, it is now in Fedora Extras (#188974) and
  tweak mesa-6.5.1-build-config.patch to not build libGLw.
- Drop mesa-6.5.1-r300-smooth-line.patch, the smooth line fallback can
  now be prevented by enabling disable_lowimpact_fallback in
  /etc/drirc.
- Drop mesa-6.4.1-radeon-use-right-texture-format.patch, now upstream.
- Drop mesa-6.5-drop-static-inline.patch, workaround no longer necessary.
* Thu Sep  7 2006 Kristian Høgsberg <krh@redhat.com>
- Drop unused mesa-modular-dri-dir.patch.
* Tue Aug 29 2006 Kristian Høgsberg <krh@redhat.com> - 6.5.1-0.rc2.fc6
- Rebase to 6.5.1 RC2.
- Get rid of redhat-mesa-driver-install and redhat-mesa-target helper
  scripts and clean up specfile a bit.
* Mon Aug 28 2006 Kristian Høgsberg <krh@redhat.com> - 6.5.1-0.rc1.2.fc6
- Drop upstreamed patches mesa-6.5-texture-from-pixmap-fixes.patch and
  mesa-6.5-tfp-fbconfig-attribs.patch and fix
  mesa-6.4.1-radeon-use-right-texture-format.patch to not break 16bpp
  transparency.
* Fri Aug 25 2006 Adam Jackson <ajackson@redhat.com> - 6.5.1-0.rc1.1.fc6
- mesa-6.5.1-build-config.patch: Add i965 to x86-64 config.
* Wed Aug 23 2006 Kristian Høgsberg <krh@redhat.com> - 6.5.1-0.rc1.fc6
- Bump to 6.5.1 RC1.
* Tue Aug 22 2006 Kristian Høgsberg <krh@redhat.com> 6.5-26.20060818cvs.fc6
- Pull the vtxfmt patch into the selinux-awareness patch, handle exec
  mem heap init failure correctly by releasing mutex.
* Tue Aug 22 2006 Adam Jackson <ajackson@redhat.com> 6.5-25.20060818cvs.fc6
- mesa-6.5.1-r300-smooth-line.patch: Added, fakes smooth lines with aliased
  lines on R300+ cards, makes Google Earth tolerable.
- mesa-6.5-force-r300.patch: Resurrect.
* Tue Aug 22 2006 Adam Jackson <ajackson@redhat.com> 6.5-24.20060818cvs.fc6
- mesa-6.5.1-radeon-vtxfmt-cleanup-properly.patch: Fix a segfault on context
  destruction when selinux is enabled.
* Mon Aug 21 2006 Adam Jackson <ajackson@redhat.com> 6.5-23.20060818cvs.fc6
- redhat-mesa-driver-install: Reenable installing the tdfx driver. (#203295)
* Fri Aug 18 2006 Adam Jackson <ajackson@redhat.com> 6.5-22.20060818cvs.fc6
- Update to pre-6.5.1 snapshot.
- Re-add libOSMesa{,16,32}. (#186366)
- Add BuildReq: on libXp-devel due to openmotif header insanity.
* Sun Aug 13 2006 Florian La Roche <laroche@redhat.com> 6.5-21.fc6
- fix one Requires: to use the correct mesa-libGLw name
* Thu Jul 27 2006 Mike A. Harris <mharris@redhat.com> 6.5-20.fc6
- Conditionalized libGLw inclusion with new with_libGLw macro defaulting
  to 1 (enabled) for now, however since nothing in Fedora Core uses libGLw
  anymore, we will be transitioning libGLw to an external package maintained
  in Fedora Extras soon.
* Wed Jul 26 2006 Kristian Høgsberg <krh@redhat.com> 6.5-19.fc5.aiglx
- Build for fc5 aiglx repo.
* Tue Jul 25 2006 Adam Jackson <ajackson@redhat.com> 6.5-19.fc6
- Disable TLS dispatch, it is selinux-hostile.
* Tue Jul 25 2006 Adam Jackson <ajackson@redhat.com> 6.5-18.fc6
- mesa-6.5-fix-glxinfo-link.patch: lib64 fix.
* Tue Jul 25 2006 Adam Jackson <ajackson@redhat.com> 6.5-17.fc6
- mesa-6.5-fix-linux-indirect-build.patch: Added.
- mesa-6.5-fix-glxinfo-link.patch: Added.
- Build libOSMesa never instead of inconsistently; to be fixed later.
- Updates to redhat-mesa-target:
  - Always select linux-indirect when not building for DRI
  - Enable DRI to be built on PPC64 (still disabled in the spec file though)
  - MIT licence boilerplate
* Tue Jul 25 2006 Mike A. Harris <mharris@redhat.com> 6.5-16.fc6
- Remove glut-devel dependency, as nothing actually uses it that we ship.
- Added mesa-6.5-dont-libglut-me-harder-ok-thx-bye.patch to prevent libglut
  and other libs from being linked into glxgears/glxinfo even though they
  are not actually used.  This was the final package linking to freeglut in
  Fedora Core, blocking freeglut from being moved to Extras.
- Commented all of the virtual provides in the spec file to document clearly
  how they should be used by other developers in specifying build and runtime
  dependencies when packaging software which links to libGL, libGLU, and
  libGLw. (#200069)
* Mon Jul 24 2006 Adam Jackson <ajackson@redhat.com> 6.5-15.fc6
- Attempt to add selinux awareness; check if we can map executable memory
  and fail softly if not.  Removes the need for allow_execmem from huge
  chunks of the desktop.
- Disable the r300 gart fix for not compiling.
* Mon Jul 24 2006 Kristian Høgsberg <krh@redhat.com> 6.5-14.fc6
- Add mesa-6.5-r300-free-gart-mem.patch to make r300 driver free gart
  memory on context destroy.
* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 6.5-13.1.fc6
- rebuild
* Wed Jul  5 2006 Mike A. Harris <mharris@redhat.com> 6.5-13.fc6
- Added mesa-6.5-fix-opt-flags-bug197640.patch as 2nd attempt to fix OPT_FLAGS
  for (#197640).
- Ensure that redhat-mesa-driver-install creates $DRIMODULE_DESTDIR with
  mode 0755.
* Wed Jul  5 2006 Mike A. Harris <mharris@redhat.com> 6.5-12.fc6
- Maybe actually, you know, apply the mesa-6.5-glx-use-tls.patch as that might
  help to you know, actually solve the problem.  Duh.
- Use {dist} tag in Release field now.
* Wed Jul  5 2006 Mike A. Harris <mharris@redhat.com> 6.5-11
- Added mesa-6.5-glx-use-tls.patch to hopefully get -DGLX_USE_TLS to really
  work this time due to broken upstream linux-dri-* configs. (#193979)
- Pass RPM_OPT_FLAGS via OPT_FLAGS instead of via CFLAGS also for (#193979)
* Mon Jun 19 2006 Mike A. Harris <mharris@redhat.com> 6.5-10
- Bump libdrm-devel dep to trigger new ExclusiveArch test with the new package.
- Use Fedora Extras style BuildRoot tag.
- Added "Requires(post): /sbin/ldconfig" and postun to all runtime lib packages.
* Mon Jun 12 2006 Kristian Høsberg <krh@redhat.com> 6.5-9
- Add mesa-6.5-fix-pbuffer-dispatch.patch to fix pbuffer marshalling code.
* Mon May 29 2006 Kristian Høgsberg <krh@redhat.com> 6.5-8
- Bump for rawhide build.
* Mon May 29 2006 Kristian Høgsberg <krh@redhat.com> 6.5-7
- Update mesa-6.5-texture-from-pixmap-fixes.patch to include new
  tokens and change tfp functions to return void.  Yes, a new mesa
  snapshot would be nice.
* Wed May 17 2006 Mike A. Harris <mharris@redhat.com> 6.5-6
- Add "BuildRequires: makedepend" for bug (#191967)
* Tue Apr 11 2006 Kristian Høgsberg <krh@redhat.com> 6.5-5
- Bump for fc5 build.
* Tue Apr 11 2006 Adam Jackson <ajackson@redhat.com> 6.5-4
- Disable R300_FORCE_R300 hack for wider testing.
* Mon Apr 10 2006 Kristian Høgsberg <krh@redhat.com> 6.5-3
- Add mesa-6.5-noexecstack.patch to prevent assembly files from making
  libGL.so have executable stack.
* Mon Apr 10 2006 Kristian Høgsberg <krh@redhat.com> 6.5-2
- Bump for fc5 build.
- Bump libdrm requires to 2.0.1.
* Sat Apr  1 2006 Kristian Høgsberg <krh@redhat.com> 6.5-1
- Update to mesa 6.5 snapshot.
- Use -MG for generating deps and some files are not yet symlinked at
  make depend time.
- Drop mesa-6.4.2-dprintf-to-debugprintf-for-bug180122.patch and
  mesa-6.4.2-xorg-server-uses-bad-datatypes-breaking-AMD64-fdo5835.patch
  as these are upstream now.
- Drop mesa-6.4.1-texture-from-drawable.patch and add
  mesa-6.5-texture-from-pixmap-fixes.patch.
- Update mesa-modular-dri-dir.patch to apply.
- Widen libGLU glob.
- Reenable r300 driver install.
- Widen libOSMesa glob.
- Go back to patching config/linux-dri, add mesa-6.5-build-config.patch,
  drop mesa-6.3.2-build-configuration-v4.patch.
- Disable sis dri driver for now, only builds on x86 and x86-64.
* Fri Mar 24 2006 Kristian Høgsberg <krh@redhat.com> 6.4.2-7
- Set ARCH_FLAGS=-DGLX_USE_TLS to enable TLS for GL contexts.
* Wed Mar  1 2006 Karsten Hopp <karsten@redhat.de> 6.4.2-6
- Buildrequires: libXt-devel (#183479)
* Sat Feb 25 2006 Mike A. Harris <mharris@redhat.com> 6.4.2-5
- Disable the expeimental r300 DRI driver, as it has turned out to cause
  instability and system hangs for many users.
* Wed Feb 22 2006 Adam Jackson <ajackson@redhat.com> 6.4.2-4
- rebuilt
* Sun Feb 19 2006 Ray Strode <rstrode@redhat.com> 6.4.2-3
- enable texture-from-drawable patch
- add glut-devel dependency
* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 6.4.2-2.1
- bump again for double-long bug on ppc(64)
* Tue Feb  7 2006 Mike A. Harris <mharris@redhat.com> 6.4.2-2
- Added new "glx-utils" subpackage with glxgears and glxinfo (#173510)
- Added mesa-6.4.2-dprintf-to-debugprintf-for-bug180122.patch to workaround
  a Mesa namespace conflict with GNU_SOURCE (#180122)
- Added mesa-6.4.2-xorg-server-uses-bad-datatypes-breaking-AMD64-fdo5835.patch
  as an attempt to fix bugs (#176976,176414,fdo#5835)
- Enabled inclusion of the *EXPERIMENTAL UNSUPPORTED* r300 DRI driver on
  x86, x86_64, and ppc architectures, however the 2D Radeon driver will soon
  be modified to require the user to manually turn experimental DRI support
  on with Option "dri" in xorg.conf to test it out and report all X bugs that
  occur while using it directly to X.Org bugzilla.  (#179712)
- Use "libOSMesa.so.6.4.0604*" glob in file manifest, to avoid having to
  update it each upstream release.
* Sat Feb  4 2006 Mike A. Harris <mharris@redhat.com> 6.4.2-1
- Updated to Mesa 6.4.2
- Use "libGLU.so.1.3.0604*" glob in file manifest, to avoid having to update it
  each upstream release.
* Tue Jan 24 2006 Mike A. Harris <mharris@redhat.com> 6.4.1-5
- Added missing "BuildRequires: expat-devel" for bug (#178525)
- Temporarily disabled mesa-6.4.1-texture-from-drawable.patch, as it fails
  to compile on at least ia64, and possibly other architectures.
* Tue Jan 17 2006 Kristian Høgsberg <krh@redhat.com> 6.4.1-4
- Add mesa-6.4.1-texture-from-drawable.patch to implement protocol
  support for GLX_EXT_texture_from_drawable extension.
* Sat Dec 24 2005 Mike A. Harris <mharris@redhat.com> 6.4.1-3
- Manually copy libGLw headers that Mesa forgets to install, to fix (#173879).
- Added mesa-6.4.1-libGLw-enable-motif-support.patch to fix (#175251).
- Removed "Conflicts" lines from libGL package, as they are "Obsoletes" now.
- Do not rename swrast libGL .so version, as it is the OpenGL version.
* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 6.4.1-2
- Rebuild to ensure libGLU gets rebuilt with new gcc with C++ compiler fixes.
- Changed the 3 devel packages to use Obsoletes instead of Conflicts for the
  packages the files used to be present in, as this is more friendy for
  OS upgrades.
- Added "Requires: libX11-devel" to mesa-libGL-devel package (#173712)
- Added "Requires: libGL-devel" to mesa-libGLU-devel package (#175253)
* Sat Dec 17 2005 Mike A. Harris <mharris@redhat.com> 6.4.1-1
- Updated MesaLib tarball to version 6.4.1 from Mesa project for X11R7 RC4.
- Added pkgconfig dependency.
- Updated "BuildRequires: libdrm-devel >= 2.0-1"
- Added Obsoletes lines to all the subpackages to have cleaner upgrades.
- Added mesa-6.4.1-amd64-assyntax-fix.patch to work around a build problem on
  AMD64, which is fixed in the 6.4 branch of Mesa CVS.
- Conditionalize libOSMesa inclusion, and default to not including it for now.
* Fri Dec  9 2005 Jesse Keating <jkeating@redhat.com> 6.4-5.1
- rebuilt
* Sun Nov 20 2005 Jeremy Katz <katzj@redhat.com> 6.4-5
- fix directory used for loading dri modules (#173679)
- install dri drivers as executable so they get stripped (#173292)
* Thu Nov  3 2005 Mike A. Harris <mharris@redhat.com> 6.4-4
- Wrote redhat-mesa-source-filelist-generator to dynamically generate the
  files to be included in the mesa-source subpackage, to minimize future
  maintenance.
- Fixed detection and renaming of software mesa .so version.
* Wed Nov  2 2005 Mike A. Harris <mharris@redhat.com> 6.4-3
- Hack: autodetect if libGL was given .so.1.5* and rename it to 1.2 for
  consistency on all architectures, and to avoid upgrade problems if we
  ever disable DRI on an arch and then re-enable it later.
* Wed Nov  2 2005 Mike A. Harris <mharris@redhat.com> 6.4-2
- Added mesa-6.4-multilib-fix.patch to instrument and attempt to fix Mesa
  bin/installmesa script to work properly with multilib lib64 architectures.
- Set and export LIB_DIR and INCLUDE_DIR in spec file 'install' section,
  and invoke our modified bin/installmesa directly instead of using
  "make install".
- Remove "include/GL/uglglutshapes.h", as it uses the GLUT license, and seems
  like an extraneous file anyway.
- Conditionalize the file manifest to include libGL.so.1.2 on DRI enabled
  builds, but use libGL.so.1.5.060400 instead on DRI disabled builds, as
  this is how upstream builds the library, although it is not clear to me
  why this difference exists yet (which was not in Xorg 6.8.2 Mesa).
* Thu Oct 27 2005 Mike A. Harris <mharris@redhat.com> 6.4-1
- Updated to new upstream MesaLib-6.4
- Updated libGLU.so.1.3.060400 entry in file manifest
- Updated "BuildRequires: libdrm-devel >= 1.0.5" to pick up fixes for the
  unichrome driver.
* Tue Sep 13 2005 Mike A. Harris <mharris@redhat.com> 6.3.2-6
- Fix redhat-mesa-driver-install and spec file to work right on multilib
  systems.
* Mon Sep  5 2005 Mike A. Harris <mharris@redhat.com> 6.3.2-5
- Fix mesa-libGL-devel to depend on mesa-libGL instead of mesa-libGLU.
- Added virtual "Provides: libGL..." entries for each subpackage as relevant.
* Mon Sep  5 2005 Mike A. Harris <mharris@redhat.com> 6.3.2-4
- Added the mesa-source subpackage, which contains part of the Mesa source
  code needed by other packages such as the X server to build stuff.
* Mon Sep  5 2005 Mike A. Harris <mharris@redhat.com> 6.3.2-3
- Added Conflicts/Obsoletes lines to all of the subpackages to make upgrades
  from previous OS releases, and piecemeal upgrades work as nicely as
  possible.
* Mon Sep  5 2005 Mike A. Harris <mharris@redhat.com> 6.3.2-2
- Wrote redhat-mesa-target script to simplify mesa build target selection.
- Wrote redhat-mesa-driver-install to install the DRI drivers and simplify
  per-arch conditionalization, etc.
* Sun Sep  4 2005 Mike A. Harris <mharris@redhat.com> 6.3.2-1
- Initial build.
