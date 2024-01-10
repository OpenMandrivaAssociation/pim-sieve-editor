%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Sieve editor for KDE PIM applications
Name:		plasma6-pim-sieve-editor
Version:	24.01.85
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/pim-sieve-editor-%{version}.tar.xz
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

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n pim-sieve-editor-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang sieveeditor
