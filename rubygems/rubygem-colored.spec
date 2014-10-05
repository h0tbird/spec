%global gem_name colored

Summary: Add some color to your life
Name: rubygem-%{gem_name}
Version: 1.2
Release: 1%{?dist}
Group: Development/Languages
License: Apache 2.0
URL: http://github.com/defunkt/colored
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems)
BuildRequires: rubygems-devel
BuildRequires: ruby(release)
BuildRequires: ruby(rubygems)
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
>> puts "this is red".red
>> puts "this is red with a blue background (read: ugly)".red_on_blue
>> puts "this is red with an underline".red.underline
>> puts "this is really bold and really blue".bold.blue
>> logger.debug "hey this is broken!".red_on_yellow     # in rails
>> puts Color.red "This is red" # but this part is mostly untested.

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
%{gem_spec}
%{gem_instdir}/LICENSE
%{gem_instdir}/README
%{gem_instdir}/Rakefile
%{gem_instdir}/test/colored_test.rb
%exclude %{gem_dir}/cache/%{gem_name}-%{version}.gem

%files doc
%doc %{gem_dir}/doc/%{gem_name}-%{version}

%changelog
* Sun Oct 05 2014 Marc Villacorta Morera <marc.villacorta@gmail.com> - 1.2-1
- Initial package
