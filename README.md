# reddit-saved-post-archival-tools

These scripts are meant to expand upon the script to export reddit saved posts [here](https://github.com/nooneswarup/export-archive-reddit-saved).  Requires Python 3.

aggregator.py pulls all of the individual links from the html files the above script generates.  If a post was a link post, it just grabs that link.  If it was a text post, it should pull any links that were in the text post.  It does **not** grab the link to the original post at this time.

imagedownloader.py goes through the list of links aggregator.py generates and will download all image links to the directory you designate.  Supports jpg, jpeg, png, gif at this time.
