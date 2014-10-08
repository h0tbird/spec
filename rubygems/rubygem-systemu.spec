%global gem_name systemu

Summary: systemu
Name: rubygem-%{gem_name}
Version: 2.5.2
Release: 1%{?dist}
Group: Development/Languages
License: same as ruby's
URL: https://github.com/ahoward/systemu
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
BuildRequires: rubygems-devel
BuildRequires: ruby(release)
BuildRequires: ruby(rubygems)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
universal capture of stdout and stderr and handling of child process pid for
windows, *nix, etc.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for %{name}

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/samples
%{gem_instdir}/test
%{gem_instdir}/LICENSE
%{gem_instdir}/README
%{gem_instdir}/README.erb
%{gem_instdir}/Rakefile
%{gem_instdir}/systemu.gemspec
%{gem_spec}
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}

%changelog
* Wed Oct 08 2014 Marc Villacorta Morera <marc.villacorta@gmail.com> - 2.5.2-1
- Initial package
