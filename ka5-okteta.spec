%define		orgname		okteta
%define		_state		stable
%define		qtver		5.12.0

Summary:	okteta - Binary file editor
Summary(pl.UTF-8):	okteta - Edytor plików binarnych
Name:		ka5-okteta
Version:	0.26.7
Release:	1
Epoch:		1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://download.kde.org/%{_state}/%{orgname}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	ee072bf945363e088dba81561567e51e
URL:		http://www.kde.org/
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Designer-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5ScriptTools-devel
BuildRequires:	Qt5UiTools-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	kf5-attica-devel
BuildRequires:	kf5-extra-cmake-modules
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kbookmarks-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kcodecs-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-kjobwidgets-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-kparts-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-ktextwidgets-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-solid-devel
BuildRequires:	kf5-sonnet-devel
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
Requires:	%{name} = %{epoch}:%{version}-%{release}
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

%find_lang %{orgname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/okteta
%attr(755,root,root) %{_libdir}/qt5/plugins/designer/oktetawidgets.so
%{_desktopdir}/org.kde.okteta.desktop
%{_datadir}/metainfo/org.kde.okteta.appdata.xml
%lang(de) %{_docdir}/HTML/de/okteta
%lang(en) %{_docdir}/HTML/en/okteta
%lang(es) %{_docdir}/HTML/es/okteta
%lang(it) %{_docdir}/HTML/it/okteta
%lang(nl) %{_docdir}/HTML/nl/okteta
%lang(pt) %{_docdir}/HTML/pt/okteta
%lang(pt_BR) %{_docdir}/HTML/pt_BR/okteta
%lang(sr) %{_docdir}/HTML/sr/okteta
%lang(sr@latin) %{_docdir}/HTML/sr@latin/okteta
%lang(sv) %{_docdir}/HTML/sv/okteta
%lang(uk) %{_docdir}/HTML/uk/okteta
%{_datadir}/okteta
%{_iconsdir}/hicolor/*x*/apps/okteta.png
%{_datadir}/mime/packages/okteta.xml

%attr(755,root,root) %{_bindir}/struct2osd
%ghost %{_libdir}/libKasten4Controllers.so.0
%attr(755,root,root) %{_libdir}/libKasten4Controllers.so.*.*.*
%ghost %{_libdir}/libKasten4Core.so.0
%attr(755,root,root) %{_libdir}/libKasten4Core.so.*.*.*
%ghost %{_libdir}/libKasten4Gui.so.0
%attr(755,root,root) %{_libdir}/libKasten4Gui.so.*.*.*
%ghost %{_libdir}/libKasten4Okteta2Controllers.so.0
%attr(755,root,root) %{_libdir}/libKasten4Okteta2Controllers.so.*.*.*
%ghost %{_libdir}/libKasten4Okteta2Core.so.0
%attr(755,root,root) %{_libdir}/libKasten4Okteta2Core.so.*.*.*
%ghost %{_libdir}/libKasten4Okteta2Gui.so.0
%attr(755,root,root) %{_libdir}/libKasten4Okteta2Gui.so.*.*.*
%ghost %{_libdir}/libOkteta3Core.so.0
%attr(755,root,root) %{_libdir}/libOkteta3Core.so.*.*.*
%ghost %{_libdir}/libOkteta3Gui.so.0
%attr(755,root,root) %{_libdir}/libOkteta3Gui.so.*.*.*
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/parts/oktetapart.so
%{_datadir}/config.kcfg/structureviewpreferences.kcfg
%{_datadir}/knsrcfiles/okteta-structures.knsrc
%{_datadir}/kservices5/oktetapart.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/KastenControllers
%{_includedir}/KastenCore
%{_includedir}/KastenGui
%{_includedir}/OktetaCore
%{_includedir}/OktetaGui
%{_includedir}/OktetaKastenControllers
%{_includedir}/OktetaKastenCore
%{_includedir}/OktetaKastenGui
%{_libdir}/cmake/KastenControllers
%{_libdir}/cmake/KastenCore
%{_libdir}/cmake/KastenGui
%{_libdir}/cmake/OktetaCore
%{_libdir}/cmake/OktetaGui
%{_libdir}/cmake/OktetaKastenControllers
%{_libdir}/cmake/OktetaKastenCore
%{_libdir}/cmake/OktetaKastenGui
%{_libdir}/libKasten4Controllers.so
%{_libdir}/libKasten4Core.so
%{_libdir}/libKasten4Gui.so
%{_libdir}/libKasten4Okteta2Controllers.so
%{_libdir}/libKasten4Okteta2Core.so
%{_libdir}/libKasten4Okteta2Gui.so
%{_libdir}/libOkteta3Core.so
%{_libdir}/libOkteta3Gui.so
%{_pkgconfigdir}/OktetaCore.pc
%{_pkgconfigdir}/OktetaGui.pc
%{_libdir}/qt5/mkspecs/modules/qt_OktetaCore.pri
%{_libdir}/qt5/mkspecs/modules/qt_OktetaGui.pri
