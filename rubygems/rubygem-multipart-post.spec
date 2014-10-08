%global gem_name multipart-post

Summary: A multipart form post accessory for Net::HTTP
Name: rubygem-%{gem_name}
Version: 1.2.0
Release: 1%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/nicksieger/multipart-post
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
BuildRequires: rubygems-devel
BuildRequires: ruby(release)
BuildRequires: ruby(rubygems)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Use with Net::HTTP to do multipart form posts. IO values that have
content_type, original_filename, and local_path will be posted as a binary
file.

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
%{gem_instdir}/History.txt
%{gem_instdir}/Manifest.txt
%{gem_instdir}/Rakefile
%{gem_instdir}/multipart-post.gemspec
%{gem_instdir}/test
%{gem_instdir}/Gemfile.lock
%{gem_instdir}/README.txt
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}

%changelog
* Wed Oct 08 2014 Marc Villacorta Morera <marc.villacorta@gmail.com> - 1.2.0-1
- Initial package
