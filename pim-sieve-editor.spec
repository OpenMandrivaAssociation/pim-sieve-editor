#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Sieve editor for KDE PIM applications
Name:		pim-sieve-editor
Version:	26.08.0
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/pim-sieve-editor/-/archive/%{gitbranch}/pim-sieve-editor-%{gitbranchd}.tar.bz2#/pim-sieve-editor-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/pim-sieve-editor-%{version}.tar.xz
%endif
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
BuildRequires:	cmake(KF6TextAddonsWidgets)
BuildRequires:	cmake(KF6TextAutoGenerateText)
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	pkgconfig(Qt6Network)
BuildRequires:	pkgconfig(Qt6Test)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	cmake(Qt6Keychain)
BuildRequires:	cmake(KF6UserFeedback)
BuildRequires:	%mklibname -d KF6UserFeedbackWidgets

%rename plasma6-pim-sieve-editor

BuildSystem:	cmake
BuildOption:	-DBUILD_PYTHON_BINDINGS:BOOL=OFF
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%prep -a
sed -i 's/X-KDE-Sieve;/X-KDE-Sieve;X-KDE-More;/' src/data/org.kde.sieveeditor.desktop

%description
Sieve editor for KDE PIM applications.

%files -f %{name}.lang
%{_datadir}/metainfo/org.kde.sieveeditor.appdata.xml
%{_datadir}/applications/org.kde.sieveeditor.desktop
%{_bindir}/sieveeditor
%{_datadir}/config.kcfg/sieveeditorglobalconfig.kcfg
%{_datadir}/qlogging-categories6/sieveeditor.categories
%{_datadir}/qlogging-categories6/sieveeditor.renamecategories
%{_libdir}/libsieveeditor.so*
%{_datadir}/icons/*/*/*/sieveeditor.*
