%global gem_name faraday_middleware

Summary: Various middleware for Faraday
Name: rubygem-%{gem_name}
Version: 0.9.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/lostisland/faraday_middleware
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) >= 1.3.5
Requires: rubygem(faraday) >= 0.7.4
Requires: rubygem(faraday) < 0.10
BuildRequires: rubygems-devel
BuildRequires: ruby(release)
BuildRequires: ruby(rubygems) >= 1.3.5
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Various middleware for Faraday.

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
%{gem_instdir}/spec
%{gem_spec}
%{gem_instdir}/CHANGELOG.md
%{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/LICENSE.md
%{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/faraday_middleware.gemspec
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}

%changelog
* Sun Oct 05 2014 Marc Villacorta Morera <marc.villacorta@gmail.com> - 0.9.1-1
- Initial package
