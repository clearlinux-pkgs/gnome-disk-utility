#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-disk-utility
Version  : 43.0
Release  : 23
URL      : https://download.gnome.org/sources/gnome-disk-utility/43/gnome-disk-utility-43.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-disk-utility/43/gnome-disk-utility-43.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-disk-utility-bin = %{version}-%{release}
Requires: gnome-disk-utility-data = %{version}-%{release}
Requires: gnome-disk-utility-libexec = %{version}-%{release}
Requires: gnome-disk-utility-license = %{version}-%{release}
Requires: gnome-disk-utility-locales = %{version}-%{release}
Requires: gnome-disk-utility-man = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(libhandy-1)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(pwquality)
BuildRequires : pkgconfig(udisks2)
Patch1: nodvd.patch

%description
# gnome-disk-utility
This gnome-disk-utility repository provides libraries and applications for
dealing with storage devices.

%package bin
Summary: bin components for the gnome-disk-utility package.
Group: Binaries
Requires: gnome-disk-utility-data = %{version}-%{release}
Requires: gnome-disk-utility-libexec = %{version}-%{release}
Requires: gnome-disk-utility-license = %{version}-%{release}

%description bin
bin components for the gnome-disk-utility package.


%package data
Summary: data components for the gnome-disk-utility package.
Group: Data

%description data
data components for the gnome-disk-utility package.


%package libexec
Summary: libexec components for the gnome-disk-utility package.
Group: Default
Requires: gnome-disk-utility-license = %{version}-%{release}

%description libexec
libexec components for the gnome-disk-utility package.


%package license
Summary: license components for the gnome-disk-utility package.
Group: Default

%description license
license components for the gnome-disk-utility package.


%package locales
Summary: locales components for the gnome-disk-utility package.
Group: Default

%description locales
locales components for the gnome-disk-utility package.


%package man
Summary: man components for the gnome-disk-utility package.
Group: Default

%description man
man components for the gnome-disk-utility package.


%prep
%setup -q -n gnome-disk-utility-43.0
cd %{_builddir}/gnome-disk-utility-43.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663951889
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-disk-utility
cp %{_builddir}/gnome-disk-utility-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-disk-utility/4cc77b90af91e615a64ae04893fdffa7939db84c || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-disk-utility

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-disk-image-mounter
/usr/bin/gnome-disks

%files data
%defattr(-,root,root,-)
/usr/share/applications/gnome-disk-image-mounter.desktop
/usr/share/applications/gnome-disk-image-writer.desktop
/usr/share/applications/org.gnome.DiskUtility.desktop
/usr/share/dbus-1/services/org.gnome.DiskUtility.service
/usr/share/glib-2.0/schemas/org.gnome.Disks.gschema.xml
/usr/share/icons/hicolor/scalable/apps/gnome-disks-state-standby-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/org.gnome.DiskUtility-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/org.gnome.DiskUtility.Devel.svg
/usr/share/icons/hicolor/scalable/apps/org.gnome.DiskUtility.svg
/usr/share/metainfo/org.gnome.DiskUtility.appdata.xml

%files libexec
%defattr(-,root,root,-)
/usr/libexec/gsd-disk-utility-notify

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-disk-utility/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gnome-disk-image-mounter.1
/usr/share/man/man1/gnome-disks.1

%files locales -f gnome-disk-utility.lang
%defattr(-,root,root,-)

