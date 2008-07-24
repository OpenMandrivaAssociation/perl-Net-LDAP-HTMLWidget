%define module      Net-LDAP-HTMLWidget
%define name        perl-%{module}
%define version     0.07
%define release     %mkrel 3

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Like FromForm but with Net::LDAP and HTML::Widget
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%module/
Source:		http://search.cpan.org/CPAN/authors/id/M/MR/MRAMBERG/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:  perl-devel >= 0:5.600
%endif
BuildRequires:	perl(DBIx::Class::HTMLWidget)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Something like Class::DBI::FromForm / Class::DBI::FromCGI but using
HTML::Widget for form creation and validation and Net::LDAP.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/Net/LDAP/HTMLWidget.pm
%{_mandir}/*/*


