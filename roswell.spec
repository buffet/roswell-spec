Name:           roswell
Version:        22.12.14.113
Release:        %{autorelease}
Summary:        intended to be a launcher for a major lisp environment that just works

License:        MIT
URL:            https://roswell.github.io/
Source0:        https://github.com/roswell/roswell/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  libcurl-devel
BuildRequires:  make

%description
Roswell is a Lisp implementation installer/manager, launcher, and much more!


%prep
%autosetup


%build
sh bootstrap
%configure
%make_build


%install
%make_install


%files
%{_bindir}/ros
%{_sysconfdir}/roswell
%{_mandir}/man1/ros-asdf.1.*
%{_mandir}/man1/ros-build.1.*
%{_mandir}/man1/ros-checkout.1.*
%{_mandir}/man1/ros-client.1.*
%{_mandir}/man1/ros-config.1.*
%{_mandir}/man1/ros-delete.1.*
%{_mandir}/man1/ros-dump.1.*
%{_mandir}/man1/ros-emacs.1.*
%{_mandir}/man1/ros-help.1.*
%{_mandir}/man1/ros-init.1.*
%{_mandir}/man1/ros-install.1.*
%{_mandir}/man1/ros-list.1.*
%{_mandir}/man1/ros-run.1.*
%{_mandir}/man1/ros-serve.1.*
%{_mandir}/man1/ros-setup.1.*
%{_mandir}/man1/ros-template.1.*
%{_mandir}/man1/ros-update.1.*
%{_mandir}/man1/ros-use.1.*
%{_mandir}/man1/ros-wait.1.*
%{_mandir}/man1/ros.1.*

%license COPYING
%doc AUTHORS ChangeLog HACKING.md INSTALL.md NEWS  README.md


%changelog
* Sat Sep 02 2023 buffet <niclas@countingsort.com>
- Init at 22.12.14.113
