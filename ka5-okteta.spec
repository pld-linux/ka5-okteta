%define		orgname		okteta
%define		_state		stable
%define		qtver		5.5.1

Summary:	okteta - Binary file editor
Summary(pl.UTF-8):	okteta - Edytor plików binarnych
Name:		ka5-okteta
Version:	16.12.1
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://download.kde.org/%{_state}/applications/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	e122c901b5b3348d4b9aed7f9386231c
URL:		http://www.kde.org/
BuildRequires:	Qt5Designer-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5ScriptTools-devel
BuildRequires:	Qt5UiTools-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kbookmarks-devel
BuildRequires:	kf5-kcodecs-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-extra-cmake-modules
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kjobwidgets-devel
BuildRequires:	kf5-kparts-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-solid-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-attica-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-sonnet-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	qca-qt5-devel
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	shared-mime-info
Obsoletes:	kde4-kdesdk-okteta
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The program Okteta is another implementation of a standalone, plain
old-fashioned hex editor. It is based on the libkakao framework, with
plugins using the basic Okteta core and gui libraries.

%description -l pl.UTF-8
Okteta to kolejna implementacja samodzielnego, tradycyjnego edytora
szesnastkowego. Jest oparty na szkielecie libkakao z wtyczkami
wykorzystującymi biblioteki core i gui Okteta.

%package devel
Summary:	Header files for compiling applications that use okteta libraries
Summary(pl.UTF-8):	Pliki nagłówkowe do kompilacji aplikacji używających bibliotek okteta
Summary(pt_BR.UTF-8):	Arquivos de inclusão para as bibliotecas do okteta
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Widgets-devel >= %{qtver}
Requires:	kf5-kio-devel >= 5.24.0

%description devel
This package includes the header files you will need to compile
applications that use okteta libraries.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe niezbędne do kompilacji aplikacji
używających bibliotek okteta.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão para desenvolvimento e compilação de programas
que usem as bibliotecas do okteta.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/okteta
%attr(755,root,root) %{_libdir}/qt5/plugins/oktetapart.so
%attr(755,root,root) %ghost %{_libdir}/libokteta2core.so.?
%attr(755,root,root) %{_libdir}/libokteta2core.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libokteta2gui.so.?
%attr(755,root,root) %{_libdir}/libokteta2gui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkasten3okteta1core.so.?
%attr(755,root,root) %{_libdir}/libkasten3okteta1core.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkasten3okteta1controllers.so.?
%attr(755,root,root) %{_libdir}/libkasten3okteta1controllers.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkasten3okteta1gui.so.?
%attr(755,root,root) %{_libdir}/libkasten3okteta1gui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkasten3core.so.?
%attr(755,root,root) %{_libdir}/libkasten3core.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkasten3controllers.so.?
%attr(755,root,root) %{_libdir}/libkasten3controllers.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkasten3gui.so.?
%attr(755,root,root) %{_libdir}/libkasten3gui.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/oktetadesignerplugin.so
%{_desktopdir}/org.kde.okteta.desktop
%{_datadir}/appdata/org.kde.okteta.appdata.xml
%{_datadir}/config.kcfg/structviewpreferences.kcfg
%{_docdir}/HTML/en/okteta
%dir %{_datadir}/kxmlgui5/oktetapart
%{_datadir}/kxmlgui5/oktetapart/oktetapartbrowserui.rc
%{_datadir}/kxmlgui5/oktetapart/oktetapartreadonlyui.rc
%{_datadir}/kxmlgui5/oktetapart/oktetapartreadwriteui.rc
%{_datadir}/kxmlgui5/okteta
%{_datadir}/okteta
%{_iconsdir}/hicolor/*x*/apps/okteta.png
%{_datadir}/mime/packages/okteta.xml
%{_sysconfdir}/xdg/okteta-structures.knsrc

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/struct2osd
%attr(755,root,root) %{_libdir}/libokteta2gui.so
%attr(755,root,root) %{_libdir}/libokteta2core.so
%attr(755,root,root) %{_libdir}/libkasten3controllers.so
%attr(755,root,root) %{_libdir}/libkasten3core.so
%attr(755,root,root) %{_libdir}/libkasten3gui.so
%attr(755,root,root) %{_libdir}/libkasten3okteta1controllers.so
%attr(755,root,root) %{_libdir}/libkasten3okteta1core.so
%attr(755,root,root) %{_libdir}/libkasten3okteta1gui.so
%{_includedir}/Okteta
%{_includedir}/Kasten
%{_includedir}/okteta
%{_includedir}/kasten
%{_libdir}/cmake/*
