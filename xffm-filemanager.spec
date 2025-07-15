Summary:	Xffm-filemanager - filemanager
Summary(pl.UTF-8):	Xffm-filemanager - zarządca plików
Name:		xffm-filemanager
Version:	4.5.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/xffm/%{name}-%{version}.tar.gz
# Source0-md5:	d5c94b8688d800a16b8ed8269fa33249
Patch0:		%{name}-desktop.patch
URL:		http://xffm.sourceforge.net/xffm-filemanager.html
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxffm-devel >= 4.5.0
BuildRequires:	libxml2-devel >= 2.4.0
BuildRequires:	pkgconfig
BuildRequires:	xffm-gui-devel >= 4.5.0
Provides:	xffm
Obsoletes:	xffm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Xffm-filemanager is a filemanager with three different GUI's:
- a spatial iconview
- a desktop view for ~/Desktop folder (or other)
- a treeview

%description -l pl.UTF-8
Xffm-filemanager jest zarządcą plików z trzema różnymi GUI:
- przestronny widok ikon
- widok biurka dla katalogu ~/Desktop (lub innego)
- widok drzewa

%package devel
Summary:	Xffm-filemanager development files
Summary(pl.UTF-8):	Pliki programistyczne Xffm-filemanager
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xffm-gui-devel >= 4.5.0

%description devel
Development files for Xffm-filemanager.

%description devel -l pl.UTF-8
Pliki programistyczne dla Xffm-filemanager.

%prep
%setup -q
%patch -P0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/xffm/plugins

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xffm/mcs-shm/libxffmsettings.la

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/nb{_NO,}
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/pt{_PT,}
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/no

rm -rf $RPM_BUILD_ROOT%{_datadir}/xffm

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/xffm-deskview
%attr(755,root,root) %{_bindir}/xffm-iconview
%attr(755,root,root) %{_bindir}/xffm-root
%attr(755,root,root) %{_bindir}/xffm-treeview
%dir %{_libdir}/xffm
%dir %{_libdir}/xffm/mcs-shm
%dir %{_libdir}/xffm/plugins
%attr(755,root,root) %{_libdir}/xffm/mcs-shm/libxffmsettings.so
%{_desktopdir}/Xffm-filemanager.desktop
%{_desktopdir}/Xffm-find.desktop
%{_desktopdir}/Xffm-iconview.desktop
%{_desktopdir}/Xffm-root.desktop
%{_desktopdir}/Xffm-treeview.desktop
%{_pixmapsdir}/*.png

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/xffm-filemanager.pc
