%define url_ver %(echo %{version}|cut -d. -f1,2)
%define oname   mate-file-archiver

Summary:	An archive manager for MATE Desktop
Name:		engrampa
Version:	1.18.2
Release:	1
Group:		Archiving/Compression
License:	GPLv2+ and LGPLv2+
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	yelp-tools
BuildRequires:	magic-devel
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libcaja-extension)
BuildRequires:	pkgconfig(sm)
Suggests:	cdrecord-isotools
# for the gsettings schema
Requires:	caja
%rename %{oname}

%description
Engrampa is an archive manager for the GNOME environment.  This means that 
you can: create and modify archives; view the content of an archive; view a 
file contained in the archive; extract files from the archive.
Engrampa is only a front-end (a graphical interface) to archiving programs 
like tar and zip. The supported file types are:
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
%setup -q

%build
%configure \
	--enable-packagekit \
	--enable-caja-actions \
	%{nil}
%make

%install
%makeinstall_std

# locales
%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc README COPYING NEWS AUTHORS
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_libexecdir}/%{name}-server
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.mate.engrampa.gschema.xml
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_libdir}/caja/extensions-2.0/libcaja-%{name}.so
%{_datadir}/appdata/engrampa.appdata.xml
%{_datadir}/caja/extensions/libcaja-engrampa.caja-extension
%{_datadir}/dbus-1/services/org.mate.Engrampa.service
%{_mandir}/man1/engrampa.1*

