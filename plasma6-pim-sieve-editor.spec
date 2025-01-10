#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Sieve editor for KDE PIM applications
Name:		plasma6-pim-sieve-editor
Version:	24.12.1
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/pim-sieve-editor/-/archive/%{gitbranch}/pim-sieve-editor-%{gitbranchd}.tar.bz2#/pim-sieve-editor-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/pim-sieve-editor-%{version}.tar.xz
%endif
Patch0:		pim-sieve-editor-More-menu.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Crash)
BuildRequires:	cmake(KF6Bookmarks)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KPim6TextEdit)
BuildRequires:	cmake(KPim6MailTransport)
BuildRequires:	cmake(KPim6PimCommon)
BuildRequires:	cmake(KPim6KSieve)
BuildRequires:	cmake(KPim6IMAP)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	cmake(Qt6Keychain)
BuildRequires:	cmake(KF6UserFeedback)
BuildRequires:	%mklibname -d KF6UserFeedbackWidgets

%description
Sieve editor for KDE PIM applications.

%files -f sieveeditor.lang
%{_datadir}/metainfo/org.kde.sieveeditor.appdata.xml
%{_datadir}/applications/org.kde.sieveeditor.desktop
%{_bindir}/sieveeditor
%{_datadir}/config.kcfg/sieveeditorglobalconfig.kcfg
%{_docdir}/*/*/sieveeditor
%{_datadir}/qlogging-categories6/sieveeditor.categories
%{_datadir}/qlogging-categories6/sieveeditor.renamecategories
%{_libdir}/libsieveeditor.so*
%{_datadir}/icons/*/*/*/sieveeditor.*

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n pim-sieve-editor-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang sieveeditor
