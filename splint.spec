%include	/usr/lib/rpm/macros.perl
Summary:	A tool for statically checking C programs
Summary(pl):	Narzêdzie do statycznego sprawdzania programów w C
Name:		splint
Version:	3.1.1
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://www.splint.org/downloads/%{name}-%{version}.src.tgz
# Source0-md5:	91635d98644312302f6f16abe73c2474
URL:		http://www.splint.org/
BuildRequires:	automake
BuildRequires:	rpm-perlprov
Obsoletes:	lclint
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Splint is a tool for statically checking C programs for security
vulnerabilities and common programming mistakes. With minimal effort,
Splint can be used as a better lint(1). If additional effort is
invested adding annotations to programs, Splint can perform stronger
checks than can be done by any standard lint.

%description -l pl
Splint jest narzêdziem do statycznego sprawdzania programów w C w
zakresie naruszenia bezpieczeñstwa i popularnych b³êdów
programistycznych. Z ma³ym wysi³kiem Splint mo¿e byæ u¿ywany jako
lepszy lint(1). Przy dodatkowym wk³adzie pracy w dodawanie komentarzy
do programów Splint mo¿e wykonaæ silniejsz± kontrolê ni¿ standardowy
lint.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* config
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/splint
%{_datadir}/splint
%{_mandir}/man*/*
