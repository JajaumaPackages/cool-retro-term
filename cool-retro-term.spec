%global gitdate 20171029
%global gitversion 1.0.1
%global gitcommit b9d0272

Name:           cool-retro-term
Version:        %{gitversion}
Release:        1.git%{gitdate}.%{gitcommit}%{?dist}
Summary:        A good looking terminal emulator which mimics the old cathode display

License:        GPLv3
URL:            https://github.com/Swordfish90/cool-retro-term
Source0:        cool-retro-term.tar.bz2

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

%description
cool-retro-term is a terminal emulator which mimics the look and feel of the
old cathode tube screens. It has been designed to be eye-candy, customizable,
and reasonably lightweight.


%prep
%setup -q -n cool-retro-term


%build
%{_qt5_qmake}
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install INSTALL_ROOT=%{buildroot}


%files
%license gpl-2.0.txt gpl-3.0.txt
%doc README.md
%{_bindir}/cool-retro-term
%{_qt5_prefix}/qml/QMLTermWidget/
%{_datadir}/applications/cool-retro-term.desktop
%{_datadir}/icons/hicolor/*/apps/cool-retro-term.*


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%changelog
* Sun Oct 29 2017 Jajauma's Packages <jajauma@yandex.ru> - 1.0.1-1.git20171029.b9d0272
- Update to latest git snapshot

* Mon Jun 05 2017 Jajauma's Packages <jajauma@yandex.ru> - 1.0.0-1.git20160605.e48719f
- Initial release
