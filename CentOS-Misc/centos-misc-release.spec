%define name centos-misc-release
%define version 1
%define release 0.1
%define buildroot %{_topdir}/%{name}-%{version}-root

BuildArch: noarch
BuildRoot: %{buildroot}
Summary: Extra Packages from CentOS Misc Repository
License: GPLv3
Name: %{name}
Version: %{version}
Release: %{release}
Group: System Environment/Base

%description
Extra Packages from CentOS Misc Repository

%prep
#nop

%build
#nop

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/
cp -p ~/CentOS-Misc.repo $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/etc/yum.repos.d/CentOS-Misc.repo

%changelog
* Sun Apr 19 2015 Marc Villacorta <marc.villacorta@gmail.com> 1.0.1
- First release.
