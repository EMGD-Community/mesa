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
Obsoletes: simulator-opengl

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
Obsoletes:  simulator-opengl-devel

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
%setup -q -n %{name}-%{version} -b1

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

%post libgbm -p /sbin/ldconfig
rm -rf /usr/lib/libdricore.so
#rm -rf /usr/lib/libglsl.so
ln -sf /usr/lib/libdricore%{version}.so /usr/lib/libdricore.so
#ln -sf /usr/lib/libglsl%{version}.so /usr/lib/libglsl.so

%postun libgbm -p /sbin/ldconfig
rm -rf /usr/lib/libdricore.so
#rm -rf /usr/lib/libglsl.so

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
%{_libdir}/libdricore%{version}.so*
#%{_libdir}/libglsl%{version}.so*

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
