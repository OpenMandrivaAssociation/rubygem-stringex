%define rbname stringex

Summary:	Some [hopefully] useful extensions to Ruby's String class
Name:		rubygem-%{rbname}
Version:	1.5.1
Release:	2
License:	GPLv2+ or Ruby
Group:		Development/Ruby
Url:		https://github.com/rsl/stringex
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems
BuildArch:	noarch

%description
Some [hopefully] useful extensions to Ruby's String class. Stringex is made up
of three libraries: ActsAsUrl [permalink solution with better character
translation], Unidecoder [Unicode to Ascii transliteration], and
StringExtensions [miscellaneous helper methods for the String class].

%files
%dir %{gem_dir}/gems/%{rbname}-%{version}/lib/
%{gem_dir}/gems/%{rbname}-%{version}/lib/*
%{gem_dir}/specifications/%{rbname}-%{version}.gemspec

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%doc %{gem_dir}/gems/%{rbname}-%{version}/*.rdoc
%doc %{gem_dir}/gems/%{rbname}-%{version}/MIT-LICENSE
%doc %{gem_dir}/doc/%{rbname}-%{version}

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%gem_build

%install
%gem_install

