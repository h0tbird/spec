%global gem_name multi_json

Summary: A common interface to multiple JSON libraries
Name: rubygem-%{gem_name}
Version: 1.8.4
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://github.com/intridea/multi_json
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) >= 1.3.5
BuildRequires: rubygems-devel
BuildRequires: ruby(release)
BuildRequires: ruby(rubygems) >= 1.3.5
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
A common interface to multiple JSON libraries, including Oj, Yajl, the JSON
gem (with C-extensions), the pure-Ruby JSON gem, NSJSONSerialization, gson.rb,
JrJackson, and OkJson.

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
%{gem_instdir}/CHANGELOG.md
%{gem_instdir}/CONTRIBUTING.md
%{gem_instdir}/Gemfile
%{gem_instdir}/LICENSE.md
%{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/multi_json.gemspec
%{gem_spec}
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem
%exclude %{gem_instdir}/.document
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.yardopts

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}

%changelog
* Wed Oct 08 2014 Marc Villacorta Morera <marc.villacorta@gmail.com> - 1.8.4-1
- Initial package
