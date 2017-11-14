Summary:	Sieve editor for KDE PIM applications
Name:		pim-sieve-editor
Version:	17.08.3
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5Bookmarks)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5PimTextEdit)
BuildRequires:	cmake(KF5MailTransport)
BuildRequires:	cmake(KF5PimCommon)
BuildRequires:	cmake(KF5LibKSieve)
BuildRequires:	cmake(KF5IMAP)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
Provides:	sieveeditor = %{EVRD}
Conflicts:	sieveeditor < 3:17.04.0
Obsoletes:	sieveeditor < 3:17.04.0

%description
Sieve editor for KDE PIM applications.

%files -f sieveeditor.lang
%{_kde5_applicationsdir}/org.kde.sieveeditor.desktop
%{_bindir}/sieveeditor
%{_datadir}/config.kcfg/sieveeditorglobalconfig.kcfg
%{_datadir}/kconf_update/sieveeditor*
%{_docdir}/*/*/sieveeditor
%{_sysconfdir}/xdg/sieveeditor.categories
%{_sysconfdir}/xdg/sieveeditor.renamecategories

%dependinglibpackage sieveeditor 5

#----------------------------------------------------------------------

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang sieveeditor
