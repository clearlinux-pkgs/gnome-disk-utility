#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-disk-utility
Version  : 3.30.0
Release  : 1
URL      : https://download.gnome.org/sources/gnome-disk-utility/3.30/gnome-disk-utility-3.30.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-disk-utility/3.30/gnome-disk-utility-3.30.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: gnome-disk-utility-bin
Requires: gnome-disk-utility-data
Requires: gnome-disk-utility-license
Requires: gnome-disk-utility-locales
Requires: gnome-disk-utility-man
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : pkgconfig(libcanberra-gtk3)
BuildRequires : pkgconfig(liblzma)
BuildRequires : pkgconfig(libnotify)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(pwquality)
BuildRequires : pkgconfig(udisks2)
Patch1: nodvd.patch

%description
gnome-disk-utility provides libraries and applications for dealing
with storage devices.

%package bin
Summary: bin components for the gnome-disk-utility package.
Group: Binaries
Requires: gnome-disk-utility-data
Requires: gnome-disk-utility-license
Requires: gnome-disk-utility-man

%description bin
bin components for the gnome-disk-utility package.


%package data
Summary: data components for the gnome-disk-utility package.
Group: Data

%description data
data components for the gnome-disk-utility package.


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
%setup -q -n gnome-disk-utility-3.30.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536419432
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/doc/gnome-disk-utility
cp COPYING %{buildroot}/usr/share/doc/gnome-disk-utility/COPYING
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-disk-utility

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-disk-image-mounter
/usr/bin/gnome-disks
/usr/libexec/gsd-disk-utility-notify

%files data
%defattr(-,root,root,-)
/usr/share/applications/gnome-disk-image-mounter.desktop
/usr/share/applications/gnome-disk-image-writer.desktop
/usr/share/applications/org.gnome.DiskUtility.desktop
/usr/share/dbus-1/services/org.gnome.DiskUtility.service
/usr/share/glib-2.0/schemas/org.gnome.Disks.gschema.xml
/usr/share/icons/hicolor/16x16/apps/gnome-disks.png
/usr/share/icons/hicolor/22x22/apps/gnome-disks.png
/usr/share/icons/hicolor/24x24/apps/gnome-disks.png
/usr/share/icons/hicolor/256x256/apps/gnome-disks.png
/usr/share/icons/hicolor/32x32/apps/gnome-disks.png
/usr/share/icons/hicolor/48x48/apps/gnome-disks.png
/usr/share/icons/hicolor/scalable/apps/gnome-disks-state-standby-symbolic.svg
/usr/share/icons/hicolor/scalable/apps/gnome-disks-symbolic.svg
/usr/share/metainfo/org.gnome.DiskUtility.appdata.xml

%files license
%defattr(-,root,root,-)
/usr/share/doc/gnome-disk-utility/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/gnome-disk-image-mounter.1
/usr/share/man/man1/gnome-disks.1

%files locales -f gnome-disk-utility.lang
%defattr(-,root,root,-)

