%global gem_name r10k

Summary: Puppet environment and module deployment
Name: rubygem-%{gem_name}
Version: 1.3.4
Release: 1%{?dist}
Group: Development/Languages
License: Apache 2.0
URL: http://github.com/adrienthebo/r10k
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(colored) >= 1.2
Requires: rubygem(cri) => 2.5.0
Requires: rubygem(cri) < 2.6
Requires: rubygem(systemu) => 2.5.2
Requires: rubygem(systemu) < 2.6
Requires: rubygem(log4r) >= 1.1.10
Requires: rubygem(multi_json) => 1.8.2
Requires: rubygem(multi_json) < 1.9
Requires: rubygem(json_pure) => 1.8.1
Requires: rubygem(json_pure) < 1.9
Requires: rubygem(faraday) => 0.8.8
Requires: rubygem(faraday) < 0.9
Requires: rubygem(faraday_middleware) => 0.9.0
Requires: rubygem(faraday_middleware) < 0.10
Requires: rubygem(faraday_middleware-multi_json) => 0.0.5
Requires: rubygem(faraday_middleware-multi_json) < 0.1
BuildRequires: rubygems-devel
BuildRequires: ruby(release)
BuildRequires: ruby(rubygems) 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
R10K provides a general purpose toolset for deploying Puppet environments and modules.
It implements the Puppetfile format and provides a native implementation of Puppet
dynamic environments.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for %{name}.

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
find %{buildroot}%{gem_instdir}/bin -type f | \
  xargs -n 1 sed -i -e 's"^#!/usr/bin/env ruby"#!/usr/bin/ruby"'

%files
%{_bindir}/r10k
%dir %{gem_instdir}
%{gem_instdir}/bin
%{gem_instdir}/CHANGELOG.mkd
%{gem_instdir}/LICENSE
%{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.nodeset.yml
%exclude %{gem_instdir}/.rspec
%exclude %{gem_instdir}/.travis.yml

%files doc
%{gem_instdir}/Gemfile
%{gem_instdir}/r10k.gemspec
%{gem_instdir}/spec/
%exclude %{gem_instdir}/spec/fixtures/doc/components/.empty_directory
%doc %{gem_docdir}
%{gem_instdir}/doc/dynamic-environments.mkd
%{gem_instdir}/doc/dynamic-environments/configuration.mkd
%{gem_instdir}/doc/dynamic-environments/git-environments.markdown
%{gem_instdir}/doc/dynamic-environments/introduction.mkd
%{gem_instdir}/doc/dynamic-environments/usage.mkd
%{gem_instdir}/doc/puppetfile.markdown
%{gem_instdir}/r10k.yaml.example

%changelog
* Sun Oct 5 2014 Marc Villacorta Morera <marc.villacorta@gmail.com> - 1.3.4-1
- Initial package
