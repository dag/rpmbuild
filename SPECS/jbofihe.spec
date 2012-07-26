%global github_user zorun
%global git_treeish 2678c77

Name:		jbofihe
Version:	0.39.%{git_treeish}
Release:	1%{?dist}
Summary:	Parser & analyzer for Lojban
Group:		Applications/Text
License:	GPLv2
URL:		https://github.com/%{github_user}/%{name}

# curl https://github.com/zorun/jbofihe/tarball/2678c77 -L -o jbofihe-0.39.2678c77.tar.gz
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	perl
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gcc

%description
jbofihe is a command-line driven program with the following functions:

* checking grammatical correctness of Lojban text

* displaying successfully analyzed text with nesting of grammatical
constructs shown (either inline or as a tree)

* displaying approximate word-for-word English translations of the Lojban
words, with some limited 'part-of-speech' adjustment of the English
forms.

* showing which sumti fill each of the places of each selbri


%prep
%setup -q -n %{github_user}-%{name}-%{git_treeish}


%build
perl config.pl --prefix=/usr
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%{_bindir}/jbofihe
%{_bindir}/cmafihe
%{_bindir}/smujajgau
%{_bindir}/jvocuhadju
%{_bindir}/vlatai
%{_libdir}/jbofihe/smujmaji.dat
%attr(0644, -, -) %{_mandir}/man1/jbofihe.1.gz
%attr(0644, -, -) %{_mandir}/man1/cmafihe.1.gz
%attr(0644, -, -) %{_mandir}/man1/smujajgau.1.gz
%attr(0644, -, -) %{_mandir}/man1/jvocuhadju.1.gz
%attr(0644, -, -) %{_mandir}/man1/vlatai.1.gz


%changelog
* Thu Jul 26 2012 Dag Odenhall <dag.odenhall@gmail.com>
- created spec file
