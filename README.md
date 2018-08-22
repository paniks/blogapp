## Blogapp with Django

First try with Django framework.

### My TODO list:
- [ ] ReadMe
- [x] Install Django and get used to it (run local server, startup app, db migrations)
- [x] Posts are very important in blog-like sites, so we need create the post model
- [x] Create superuser and admin site
- [x] Add post model to admin site
- [x] Get familiar with QuertySet objects and models' managers
- [x] Create HTML templates
- [x] Create list view and detail view
- [x] Replace above views with class based views
- [x] Create URLs for models
- [ ] Send emails
- [ ] Forms with Django
- [ ] Comments system for posts
- [ ] Create tag system for post
- [ ] Get similar posts by tags
- [ ] Create own posts' filters and tags
- [ ] Sitemap
- [ ] RSS
- [ ] Search engine
- [ ] Make every thing beautiful with some boostrap
- [ ] Tests

### Requirements (for Linux Ubuntu 16.04LTS with Python3.5.2)

Update system
```bash
sudo apt-get update
sudo apt-get upgrade
```

Prepare Python 3.5 env
```bash
sudo apt-get install python3.5
sudo pip3 install virtualenv

(it's my favorite way to manage python's virtualenvs, it's not obligatory or something)
mkdir ~/venvs
cd ~/venvs/

virtualenv django-blog -p $(which python3)
```

Clone repo with https

```bash
cd directory
git clone https://github.com/paniks/blogapp.git
```

Activate virtualenv and install requirements
```bash
(in project dir)

source path/to/venv/bin/activate
pip install -r requiments.txt
```

### Usage

T.B.C.
