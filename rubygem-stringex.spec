# Generated from stringex-1.3.0.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	stringex

Summary:	Some [hopefully] useful extensions to Ruby's String class
Name:		rubygem-%{rbname}

Version:	1.5.1
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://github.com/rsl/stringex
Source0:	http://gems.rubyforge.org/gems/stringex-1.5.1.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Some [hopefully] useful extensions to Ruby's String class. Stringex is made up
of three libraries: ActsAsUrl [permalink solution with better character
translation], Unidecoder [Unicode to Ascii transliteration], and
StringExtensions [miscellaneous helper methods for the String class].

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
# %dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
# %dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/stringex
# %dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/stringex/unidecoder_data
# %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec
# %{ruby_gemdir}//gems/%{rbname}-%{version}/lib/stringex/unidecoder_data/*
# %{ruby_gemdir}//gems/%{rbname}-%{version}/lib/stringex/*.rb

%files doc
%doc %{ruby_gemdir}/gems/%{rbname}-%{version}/*.rdoc
# %doc %{ruby_gemdir}/gems/%{rbname}-%{version}/MIT-LICENSE
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}
