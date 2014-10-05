%global gem_name faraday_middleware-multi_json

Summary: Response JSON parser using MultiJson and FaradayMiddleware
Name: rubygem-%{gem_name}
Version: 0.0.6
Release: 1%{?dist}
Group: Development/Languages
License: Apache 2.0
URL: https://www.github.com/denro/faraday_middleware-multi_json
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(faraday_middleware) 
Requires: rubygem(multi_json)
BuildRequires: rubygems-devel
BuildRequires: ruby(release)
BuildRequires: ruby(rubygems)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Faraday response parser using MultiJson.

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
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_spec}
%{gem_instdir}/Gemfile
%{gem_instdir}/LICENSE
%{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%{gem_instdir}/faraday_middleware-multi_json.gemspec
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}

%changelog
* Sun Oct 05 2014 Marc Villacorta Morera <marc.villacorta@gmail.com> - 0.0.6-1
- Initial package
