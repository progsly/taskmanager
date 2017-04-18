# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.provider "virtualbox" do |vb|
    vb.name = "django_vagrant"
    # Customize the amount of memory on the VM:
    vb.memory = 512
    vb.cpus = 1
    vb.auto_nat_dns_proxy = false
    vb.customize ['modifyvm', :id, '--natdnsproxy1', 'off']
    vb.customize ['modifyvm', :id, '--natdnshostresolver1', 'on']
  end

  config.vm.box_check_update = true

  config.vm.network :private_network, ip: '192.168.33.10'
  config.vm.network :forwarded_port, guest: 80, host: 80
  config.vm.network :forwarded_port, guest: 5432, host: 5433

  #ELK

  # skip creating a local VM specific ssh key
  config.ssh.insert_key = false
  config.ssh.forward_agent = true

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder "./", "/home/vagrant/"

  #Provision
  config.vm.provision :shell, :path => "startup.sh"
  config.vm.provision :shell, inline: <<-SHELL
    sudo apt-get update
    sudo apt-get install -y python-dev
    sudo apt-get install -y libpq-dev
    sudo apt-get install -y python-pip
    sudo pip install -r requirements.txt
    python manage.py migrate
    sudo python manage.py runserver 0.0.0.0:80 &
  SHELL
end