# Traceback

{% for line in traceback %} {{ line }} {% endfor %}

# Session

{{ session }}

# Request

{{ request.environ['REMOTE_ADDR'] }}

## request.method request.url

{{ request.method }} {{ request.url }}

## request.is_xhr

{{ request.is_xhr }}

## request.json

{{ request.json | pprint }}

## request.args

{{ request.args.to_dict(flat=False) | pprint }}

## request.form

{{ request.form.to_dict(flat=False) | pprint }}

## request.cookies

{{ request.cookies | pprint }}

## request.files

{{ request.files.to_dict(flat=False) | pprint }}

## request.environ

{{ request.environ | pprint }}

# Other

It occursed at {{other.occursed_at}}.
