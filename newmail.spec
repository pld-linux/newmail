Summary:	Count unread mails in a Maildir++ directory structure
Name:		newmail
Version:	1.0
Release:	1
License:	BSD-like
Group:		Applications
Source0:	http://burningsoda.com/software/newmail/%{name}-%{version}.tgz
# Source0-md5:	f2b3f52714646f38d79e128502923596
Patch0:		%{name}-compile.patch
URL:		http://burningsoda.com/software/newmail/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
newmail is a command line utility to check for new/unread mail in a
recursive Maildir++ folder structure. It is written in pure ANSI C,
should work on any POSIX compatible system, and can be used for other
stuff—like, for example, in combination with Mutt—too.

%prep
%setup -q -n newmail
%patch0 -p1

%build
%{__cc} %{rpmcflags} newmail.c -o newmail %{rpmldflags}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}/
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install newmail $RPM_BUILD_ROOT%{_bindir}
install newmail.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE
%attr(755,root,root) %{_bindir}/newmail
%{_mandir}/man1/newmail.1*
