#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		alligator
Summary:	A convergent RSS/Atom feed reader
Summary(pl.UTF-8):	Wygodny czytnik kanałów RSS/Atom
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	d77cd5bfeed9ee26918b26aac5578412
URL:		https://apps.kde.org/alligator/
BuildRequires:	Qt5Core-devel >= 5.15.2
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel >= 5.15.9
BuildRequires:	Qt5Qml-devel >= 5.15.9
BuildRequires:	Qt5Quick-controls2-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Test
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.90.0
BuildRequires:	kf5-kconfig-devel >= 5.90.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.90.0
BuildRequires:	kf5-ki18n-devel >= 5.90.0
BuildRequires:	kf5-kirigami-addons-devel >= 0.6
BuildRequires:	kf5-syndication-devel >= 5.90.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
ExcludeArch:	x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alligator is a convergent RSS/Atom feed reader.

%description -l pl.UTF-8
Alligator to wygodny czytnik kanałów RSS/Atom.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/alligator
%{_desktopdir}/org.kde.alligator.desktop
%{_iconsdir}/hicolor/scalable/apps/alligator.svg
%{_datadir}/metainfo/org.kde.alligator.appdata.xml
