# mbox_tools

#### _Simple tools for summarizing .mbox email archives._

**`mbox-tools`** is a small collection of Python scripts to see  [`.mbox`](https://en.wikipedia.org/wiki/Mbox) files (which contain collections of email messages).

For now, it contains a single command, which transforms `.mbox` files into `.csv` digests (where each row represents a single message, and rows include basic information about an email — including its body content and a list of attachment filenames).

### Installation

To install, run `pip install mbox-tools` (preferably in a virtual machine).


### Usage

Run the following lines, where **`input_file_name`** is the (full or relative) path to your `.mbox` file and **`output_file_name`** is the path (including filename) of the `.csv` file you wish to generate:

```python
from mbox_tools import generate_csv_digest

generate_csv_digest(input_file_name, output_file_name)
```

If all goes as expected, your CSV should now be populated with as many rows as there were emails in the `.mbox` file.

The rows will have the following columns, some of which may be empty:

| Column name | May be empty? |
|:--|:--|
| from | No |
| to | No |
| cc | Yes |
| date | No |
| subject | No |
| body | Yes |
| attachments | Yes |
| priority | Yes |
| importance | Yes |
| sensitivity | Yes |


### Prior art / Caveats

`mbox-tools` would not be possible without Martin Rusev's [`mailbox`/`imbox` package](https://github.com/martinrusev). Though `mailbox` appears to have been succeeded by the refactored `imbox` (which appears to focus more on IMAP/SMTP support, and less on parsing `.mbox` files), the earlier library does much of the heavy lifting to turn `.mbox` files into cleanly-formatted Python objects.

Because of this, it may be useful to replicate this parsing within this library in the future — whether through parsing Rusev's existing logic (should we get permission, of course) or creating our own.


## Roadmap

In the process of beginning this library, we've already identified several related utilities that would be nice to have. These will be discussed in this repo's issues. Feel free to submit additional suggestions for features in the same way.


## Contributing

If you want to add to this effort, please send a pull request or open an issue! We welcome contributions of any type or size.
