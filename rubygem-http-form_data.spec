#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-http-form_data
Version  : 1.0.1
Release  : 4
URL      : https://rubygems.org/downloads/http-form_data-1.0.1.gem
Source0  : https://rubygems.org/downloads/http-form_data-1.0.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
# FormData
[![Gem Version](https://badge.fury.io/rb/http-form_data.png)](http://rubygems.org/gems/http-form_data)
[![Build Status](https://secure.travis-ci.org/httprb/form_data.rb.png?branch=master)](http://travis-ci.org/httprb/form_data.rb)
[![Code Climate](https://codeclimate.com/github/httprb/form_data.rb.png)](https://codeclimate.com/github/httprb/form_data.rb)
[![Coverage Status](https://coveralls.io/repos/httprb/form_data.rb/badge.png?branch=master)](https://coveralls.io/r/httprb/form_data.rb)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n http-form_data-1.0.1
gem spec %{SOURCE0} -l --ruby > rubygem-http-form_data.gemspec

%build
gem build rubygem-http-form_data.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
http-form_data-1.0.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/http-form_data-1.0.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/.rubocop.yml
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/CHANGES.md
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/Guardfile
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/README.md
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/http-form_data.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/lib/http/form_data.rb
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/lib/http/form_data/file.rb
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/lib/http/form_data/multipart.rb
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/lib/http/form_data/multipart/param.rb
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/lib/http/form_data/urlencoded.rb
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/lib/http/form_data/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/spec/fixtures/expected-multipart-body.tpl
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/spec/fixtures/the-http-gem.info
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/spec/lib/http/form_data/file_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/spec/lib/http/form_data/multipart_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/spec/lib/http/form_data/urlencoded_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/spec/lib/http/form_data_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/http-form_data-1.0.1/spec/support/fixtures_helper.rb
/usr/lib64/ruby/gems/2.3.0/specifications/http-form_data-1.0.1.gemspec
