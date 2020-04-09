Name:           barrier
Version:        2.3.2
Release:        1%{?dist}
Summary:        Open-source KVM software

License:        GPLv2+
URL:            https://github.com/debauchee/barrier
Source0:        https://github.com/debauchee/barrier/archive/v%{version}.tar.gz

BuildRequires:  cmake make gcc-c++ xorg-x11-server-devel libcurl-devel avahi-compat-libdns_sd-devel libXtst-devel qt5-devel openssl-devel
Requires:       qt5 avahi

%description
Barrier is software that mimics the functionality of a KVM switch, which historically would allow you to use a single keyboard and mouse to control multiple computers by physically turning a dial on the box to switch the machine you're controlling at any given moment. Barrier does this in software, allowing you to tell it which machine to control by moving your mouse to the edge of the screen, or by using a keypress to switch focus to a different system.

%prep
%autosetup -n %{name}-%{version}


%build
mkdir build
cd build
%cmake ..
%make_build


%install
rm -rf $RPM_BUILD_ROOT
cd build
%make_install
mkdir -p $RPM_BUILD_ROOT/%_mandir/man1
cp ../doc/*.1 $RPM_BUILD_ROOT/%_mandir/man1/
gzip -9 $RPM_BUILD_ROOT/%_mandir/man1/*.1

%files
%license LICENSE
%doc README.md ChangeLog doc/barrier.conf.example*
%_mandir/man1/*.1.gz
%_datadir/icons/hicolor/scalable/apps/barrier.svg
%_datadir/applications/barrier.desktop
%_bindir/barrier
%_bindir/barriers
%_bindir/barrierc


%changelog
* Thu Apr  9 2020 Piotr Rogowski <piotr.rogowski@creativestyle.pl>
- 
