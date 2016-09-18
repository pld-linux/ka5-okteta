%define		orgname		okteta
%define		_state		stable
%define		qtver		4.8.1

Summary:	okteta - Binary file editor
Summary(pl.UTF-8):	okteta - Edytor plików binarnych
Name:		kde4-okteta
Version:	4.14.3
Release:	3
License:	GPL
Group:		X11/Development/Tools
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	9a75d083a3f5ad5b6473648b43031d27
URL:		http://www.kde.org/
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	shared-mime-info
BuildRequires:	subversion-devel >= 0.37.0
BuildRequires:	utempter-devel
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
Requires:	kde4-kdebase-devel >= %{version}

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
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gimpdir}/palettes,%{_appdefsdir}}

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
%attr(755,root,root) %{_libdir}/kde4/libkbytearrayedit.so
%attr(755,root,root) %{_libdir}/kde4/oktetapart.so
%attr(755,root,root) %ghost %{_libdir}/libokteta1core.so.?
%attr(755,root,root) %{_libdir}/libokteta1core.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libokteta1gui.so.?
%attr(755,root,root) %{_libdir}/libokteta1gui.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkasten2okteta1core.so.?
%attr(755,root,root) %{_libdir}/libkasten2okteta1core.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkasten2okteta1controllers.so.?
%attr(755,root,root) %{_libdir}/libkasten2okteta1controllers.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkasten2okteta1gui.so.?
%attr(755,root,root) %{_libdir}/libkasten2okteta1gui.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/oktetadesignerplugin.so
%{_desktopdir}/kde4/okteta.desktop
%dir %{_datadir}/apps/oktetapart
%{_datadir}/apps/oktetapart/oktetapartbrowserui.rc
%{_datadir}/apps/oktetapart/oktetapartreadonlyui.rc
%{_datadir}/apps/oktetapart/oktetapartreadwriteui.rc
%{_datadir}/apps/okteta
%{_iconsdir}/hicolor/*x*/apps/okteta.png
%{_datadir}/kde4/services/kbytearrayedit.desktop
%{_datadir}/kde4/services/oktetapart.desktop
%{_kdedocdir}/en/okteta
%{_datadir}/mime/packages/okteta.xml
%{_datadir}/config/okteta-structures.knsrc
%{_datadir}/config.kcfg/structviewpreferences.kcfg
%attr(755,root,root) %ghost %{_libdir}/libkasten2core.so.?
%attr(755,root,root) %{_libdir}/libkasten2core.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkasten2controllers.so.?
%attr(755,root,root) %{_libdir}/libkasten2controllers.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libkasten2gui.so.?
%attr(755,root,root) %{_libdir}/libkasten2gui.so.*.*.*
%{_datadir}/appdata/okteta.appdata.xml

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/struct2osd.sh
%attr(755,root,root) %{_libdir}/libokteta1gui.so
%attr(755,root,root) %{_libdir}/libokteta1core.so
%attr(755,root,root) %{_libdir}/libkasten2controllers.so
%attr(755,root,root) %{_libdir}/libkasten2core.so
%attr(755,root,root) %{_libdir}/libkasten2gui.so
%attr(755,root,root) %{_libdir}/libkasten2okteta1controllers.so
%attr(755,root,root) %{_libdir}/libkasten2okteta1core.so
%attr(755,root,root) %{_libdir}/libkasten2okteta1gui.so
%{_includedir}/KDE/Okteta1
%{_includedir}/KDE/Kasten2
%{_includedir}/okteta1
%{_includedir}/kasten2
