%global gem_name json_pure

Summary: JSON Implementation for Ruby
Name: rubygem-%{gem_name}
Version: 1.8.1
Release: 1%{?dist}
Group: Development/Languages
License: Ruby
URL: http://flori.github.com/json
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
BuildRequires: rubygems-devel
BuildRequires: ruby(release)
BuildRequires: ruby(rubygems)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
This is a JSON implementation in pure Ruby.

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
%{gem_instdir}/data
%{gem_instdir}/diagrams
%{gem_instdir}/ext
%{gem_instdir}/java
%{gem_instdir}/tests
%{gem_instdir}/tools
%{gem_instdir}/CHANGES
%{gem_instdir}/COPYING
%{gem_instdir}/COPYING-json-jruby
%{gem_instdir}/GPL
%{gem_instdir}/Gemfile
%{gem_instdir}/README-json-jruby.markdown
%{gem_instdir}/Rakefile
%{gem_instdir}/TODO
%{gem_instdir}/VERSION
%{gem_instdir}/install.rb
%{gem_instdir}/json-java.gemspec
%{gem_instdir}/json.gemspec
%{gem_instdir}/json_pure.gemspec
%{gem_spec}
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/README.rdoc

%changelog
* Wed Oct 08 2014 Marc Villacorta Morera <marc.villacorta@gmail.com> - 1.8.1-1
- Initial package
