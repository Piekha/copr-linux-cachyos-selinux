Name:           uksmd
Summary:        Userspace KSM helper daemon (CachyOS branding)
Version:        1.0.0
Release:        1%{?dist}
License:        GPLv3
URL:            https://github.com/CachyOS/uksmd


Source0:        %{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  cmake
BuildRequires:  libcap-ng
BuildRequires:  libcap-ng-devel
BuildRequires:  procps-ng
BuildRequires:  procps-ng-devel
BuildRequires:  systemd
BuildRequires:  systemd-devel
Requires:       libcap-ng
Requires:       libcap-ng-devel
Requires:       procps-ng
Requires:       procps-ng-devel
%description
uksmd
%{summary}.

%prep
%setup -q -n %{name}-%{version}
%autosetup -c

%build
cd %{name}-%{version}
sed -i 's/0.64.0/0.63.3/g' meson.build
%meson
%meson_build

%install
cd %{name}-%{version}
%meson_install

%files
/usr/bin/uksmd
/usr/bin/uksmdstats
/usr/lib/debug/usr/bin/uksmd-1.0.0-1.fc37.x86_64.debug
/usr/lib/systemd/system/uksmd.service
/usr/share/licenses/uksmd/LICENSE
/usr/src/debug/uksmd-1.0.0-1.fc37.x86_64/uksmd-1.0.0/redhat-linux-build
/usr/src/debug/uksmd-1.0.0-1.fc37.x86_64/uksmd-1.0.0/uksmd.c

%changelog
* Mon Jan 30 2023 sirlucjan - 1.0.0-1
- Add uksmd for Fedora