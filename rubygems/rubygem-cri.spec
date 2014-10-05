%global gem_name cri

Summary: A library for building easy-to-use commandline tools
Name: rubygem-%{gem_name}
Version: 2.6.1
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: http://stoneship.org/software/cri/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
Requires: rubygem(colored) => 1.2
Requires: rubygem(colored) < 2
BuildRequires: rubygems-devel
BuildRequires: ruby(release)
BuildRequires: ruby(rubygems)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Cri allows building easy-to-use commandline interfaces with support for
subcommands.

%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
This package contains documentation for %{name}

%prep
%setup -q -c -T
mkdir -p .%{gem_dir}
%gem_install -n %{SOURCE0}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/lib
%{gem_spec}
%{gem_instdir}/Gemfile
%{gem_instdir}/Gemfile.lock
%{gem_instdir}/Rakefile
%{gem_instdir}/cri.gemspec
%{gem_instdir}/test
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.adoc
%doc %{gem_instdir}/NEWS.md

%changelog
* Sun Oct 05 2014 Marc Villacorta Morera <marc.villacorta@gmail.com> - 2.6.1-1
- Initial package
