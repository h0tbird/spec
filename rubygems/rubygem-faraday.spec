%global gem_name faraday

Summary: HTTP/REST API client library
Name: rubygem-%{gem_name}
Version: 0.8.8
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/lostisland/faraday
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) >= 1.3.5
Requires: rubygem(multipart-post) = 1.2.0
BuildRequires: rubygems-devel
BuildRequires: ruby(release)
BuildRequires: ruby(rubygems) >= 1.3.5
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
HTTP/REST API client library

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_instdir}/script
%{gem_instdir}/test
%{gem_spec}
%{gem_instdir}/Gemfile
%{gem_instdir}/LICENSE.md
%{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}

%changelog
* Sun Oct 05 2014 Marc Villacorta Morera <marc.villacorta@gmail.com> - 0.8.8-1
- Initial package
