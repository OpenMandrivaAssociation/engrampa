%define url_ver %(echo %{version}|cut -d. -f1,2)
%define oname   mate-file-archiver
%define name    engrampa

Name:          %{name}
Version:       1.6.0
Release:       1
Summary:       An archive manager for MATE Desktop
Group:         Archiving/Compression
License:       GPLv2+ and LGPLv2+
URL:           http://mate-desktop.org
Source0:       http://pub.mate-desktop.org/releases/%{url_ver}/%{oname}-%{version}.tar.xz

BuildRequires: intltool
BuildRequires: chrpath
BuildRequires: mate-common
BuildRequires: xsltproc
BuildRequires: which
BuildRequires: xml2po
BuildRequires: magic-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(mate-doc-utils)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libcaja-extension)
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(gsettings-desktop-schemas)

Suggests:      cdrecord-isotools
# for the gsettings schema
Requires:      caja
Provides:      %{oname} = %{version}-%{release}

%description
Engrampa is an archive manager for the GNOME environment.  This means that 
you can : create and modify archives; view the content of an archive; view a 
file contained in the archive; extract files from the archive.
Engrampa is only a front-end (a graphical interface) to archiving programs 
like tar and zip. The supported file types are :
    * Tar archives uncompressed (.tar) or compressed with
          * gzip (.tar.gz , .tgz)
          * bzip (.tar.bz , .tbz)
          * bzip2 (.tar.bz2 , .tbz2)
          * compress (.tar.Z , .taz)
          * lzop (.tar.lzo , .tzo)
          * lzma (.tar.lzma , .tlz)
    * Zip archives (.zip)
    * Jar archives (.jar , .ear , .war)
    * Lha archives (.lzh)
    * Rar archives (.rar)
    * Single files compressed with gzip, bzip, bzip2, compress, lzop, lzma
    * ISO images


%prep
%setup -q -n %{oname}-%{version}
%apply_patches

%build
NOCONFIGURE=1 ./autogen.sh
%configure2_5x                \
   --disable-scrollkeeper  \
   --disable-static        \
   --with-gtk=2.0          \
   --enable-packagekit \
   --enable-caja-actions

%make


%install
%makeinstall_std

%find_lang %{name} --with-gnome --all-name

find %{buildroot} -name "*.la" -exec rm -f {} ';'

#gw rpmlint errors
chrpath -d %{buildroot}%{_bindir}/%name
chrpath -d %{buildroot}%{_libdir}/caja/*/*.so

%files -f %{name}.lang
%doc README COPYING NEWS AUTHORS
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/MateConf/gsettings/%{name}.convert
%{_datadir}/glib-2.0/schemas/org.mate.engrampa.gschema.xml
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_libdir}/caja/extensions-2.0/libcaja-%{name}.so

