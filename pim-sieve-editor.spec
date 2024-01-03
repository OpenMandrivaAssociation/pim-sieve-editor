%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Sieve editor for KDE PIM applications
Name:		pim-sieve-editor
Version:	23.08.4
Release:	2
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Patch0:		pim-sieve-editor-More-menu.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KPim5MailTransport)
BuildRequires:	cmake(KPim5PimCommon)
BuildRequires:	cmake(KPim5LibKSieve)
BuildRequires:	cmake(KPim5IMAP)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	cmake(Qt5Keychain)
BuildRequires:	cmake(KUserFeedback)
Provides:	sieveeditor = %{EVRD}
Conflicts:	sieveeditor < 3:17.04.0
Obsoletes:	sieveeditor < 3:17.04.0

%description
Sieve editor for KDE PIM applications.

%files -f sieveeditor.lang
%{_datadir}/metainfo/org.kde.sieveeditor.appdata.xml
%{_kde5_applicationsdir}/org.kde.sieveeditor.desktop
%{_bindir}/sieveeditor
%{_datadir}/config.kcfg/sieveeditorglobalconfig.kcfg
%{_docdir}/*/*/sieveeditor
%{_datadir}/qlogging-categories5/sieveeditor.categories
%{_datadir}/qlogging-categories5/sieveeditor.renamecategories

%dependinglibpackage sieveeditor 5

#----------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang sieveeditor
