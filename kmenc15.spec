Summary:	Advanced Qt/KDE MEncoder frontend
Summary(pl.UTF-8):	Zaawansowany frontend Qt/KDE dla MEncodera
Name:		kmenc15
Version:	0.04
Release:	1
License:	GPL v2
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/kmenc15/%{name}-%{version}.tar.bz2
# Source0-md5:	64e46a32cd055516b9d82f60836eefcb
Patch0:		%{name}-build.patch
URL:		http://kmenc15.sourceforge.net/
BuildRequires:	kdelibs-devel >= 3.3
BuildRequires:	rpmbuild(macros) >= 1.167
Requires:	mencoder
Requires:	mplayer >= 3:1.0-2.pre7try2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kmenc15 is an advanced Qt/KDE MEncoder frontend, generally designed to
be a VirtualDub replacement for Linux. It is most useful for editing
and encoding large high quality AVIs capped from TV. It allows cutting
and merging at exact frames, applying any MPlayer/MEncoder filter,
with preview.

%description -l pl.UTF-8
KMenc15 to zaawansowany frontend Qt/KDE dla MEncodera, zasadniczo
zaprojektowany jako zamiennik VirtualDuba dla Linuksa. Jest
najbardziej przydatny do modyfikowania i kodowania dużych, wysokiej
jakości plików AVI nagranych z TV. Umożliwia cięcie i łączenie na
dokładnie podanych ramkach oraz stosowanie dowolnego filtru
MPlayera/MEncodera z podglądem.

%prep
%setup -q
%patch0 -p1

%build
%{__make} 	\
	CPP="%{__cxx}" \
	CFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
