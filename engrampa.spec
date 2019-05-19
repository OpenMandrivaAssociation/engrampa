%define url_ver %(echo %{version}|cut -d. -f1,2)
%define oname	mate-file-archiver

Summary:	An archive manager for MATE Desktop
Name:		engrampa
Version:	1.22.1
Release:	1
Group:		Archiving/Compression
License:	GPLv2+ and LGPLv2+
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
Patch0:		%{name}-1.18.2-port-to-libarchiver-tar.patch

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	mate-common
BuildRequires:	yelp-tools
BuildRequires:	magic-devel
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(libcaja-extension)
BuildRequires:	pkgconfig(sm)
BuildRequires:	xsltproc
BuildRequires:	yelp-tools

# for the gsettings schema
Requires:	caja

Suggests:	cdrecord-isotools

%rename		%{oname}

%description
The MATE Desktop Environment is the continuation of GNOME 2. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

MATE is under active development to add support for new technologies while
preserving a traditional desktop experience.

This package provides Engrampa, an archive manager utility for the MATE
Environment. This means that you can:
  * create and modify archives;
  * view the content of an archive;
  * view a file contained in the archive;
  * extract files from the archive.

Engrampa is only a front-end (a graphical interface) to archiving programs
like tar and zip. The supported file types are :
  * 7-Zip Compressed File (.7z)
  * WinAce Compressed File (.ace)
  * ALZip Compressed File (.alz)
  * AIX Small Indexed Archive (.ar)
  * ARJ Compressed Archive (.arj)
  * Cabinet File (.cab)
  * UNIX CPIO Archive (.cpio)
  * Debian Linux Package (.deb) [Read-only mode]
  * ISO-9660 CD Disc Image (.iso) [Read-only mode]
  * Java Archive (.jar)
  * Java Enterprise archive (.ear)
  * Java Web Archive (.war)
  * LHA Archive (.lzh, .lha)
  * WinRAR Compressed Archive (.rar)
  * RAR Archived Comic Book (.cbr)
  * RPM Linux Package (.rpm) [Read-only mode]
  * Tape Archive File:
        * uncompressed (.tar)
    or compressed with:
        * gzip (.tar.gz , .tgz)
        * bzip (.tar.bz , .tbz)
        * bzip2 (.tar.bz2 , .tbz2)
        * compress (.tar.Z , .taz)
        * lrzip (.tar.lrz , .tlrz)
        * lzip (.tar.lz , .tlz)
        * lzop (.tar.lzo , .tzo)
        * 7zip (.tar.7z)
        * xz (.tar.xz)
  * Stuffit Archives (.bin, .sit)
  * ZIP Archive (.zip)
  * ZIP Archived Comic Book (.cbz)
  * ZOO Compressed Archive File (.zoo)
  * Single files compressed with gzip, bzip, bzip2, compress, lrzip, lzip,
    lzop, rzip, xz.

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
%{_datadir}/metainfo/engrampa.appdata.xml
%{_datadir}/caja/extensions/libcaja-engrampa.caja-extension
%{_datadir}/dbus-1/services/org.mate.Engrampa.service
%{_mandir}/man1/engrampa.1*

#---------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%configure \
	--disable-schemas-compile \
	--enable-caja-actions \
	--enable-magic \
	--enable-packagekit \
	%{nil}
%make

%install
%makeinstall_std

# locales
%find_lang %{name} --with-gnome --all-name

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

