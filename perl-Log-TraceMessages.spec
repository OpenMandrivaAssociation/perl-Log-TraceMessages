%define	module	Log-TraceMessages
%define	name	perl-%{module}
%define	version	1.4
%define	release %mkrel 3

Summary:	Log::TraceMessages Perl Module
License:	GPL or Artistic
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Development/Perl
Url:		http://www.cpan.org/
Source0:	%{module}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:	perl-HTML-FromText
BuildArch:	noarch


%description
Log::TraceMessages

This module is a better way of putting 'hello there' trace messages in
your code.  It lets you turn tracing on and off without commenting out
trace statements, and provides other useful things like HTML-ified
trace messages for CGI scripts and an easy way to trace out data
structures using Data::Dumper.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Log/TraceMessages.pm
%{perl_vendorlib}/auto/Log/TraceMessages/autosplit.ix
%{_mandir}/*/*

