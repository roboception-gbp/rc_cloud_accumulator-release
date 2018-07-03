Name:           ros-indigo-rc-cloud-accumulator
Version:        1.0.3
Release:        0%{?dist}
Summary:        ROS rc_cloud_accumulator package

Group:          Development/Libraries
License:        BSD
URL:            https://wiki.ros.org/rc_cloud_accumulator
Source0:        %{name}-%{version}.tar.gz

Requires:       pcl-devel
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-pcl-ros
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-srvs
Requires:       ros-indigo-tf2
Requires:       ros-indigo-tf2-msgs
Requires:       ros-indigo-tf2-ros
BuildRequires:  pcl-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-pcl-ros
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-srvs
BuildRequires:  ros-indigo-tf2
BuildRequires:  ros-indigo-tf2-msgs
BuildRequires:  ros-indigo-tf2-ros

%description
A viewer for the SLAM component of roboception based on ROS and PCL

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Jul 03 2018 Felix Endres <felix.endres@roboception.de> - 1.0.3-0
- Autogenerated by Bloom

* Tue Jun 26 2018 Felix Endres <felix.endres@roboception.de> - 1.0.2-0
- Autogenerated by Bloom

* Fri Jun 15 2018 Felix Endres <felix.endres@roboception.de> - 1.0.0-0
- Autogenerated by Bloom

