# CadTable2CSV
Cad Tables to CSV

author:方正
email:1171153217@qq.com

这个工具旨在处理DXF文件并从ACAD_TABLE实体中提取文本数据。它还包括使用加密MAC地址管理用户身份验证的功能。

功能
DXF处理：从DXF文件中的ACAD_TABLE实体提取文本数据并保存为CSV文件。

用户身份验证：使用加密的MAC地址验证用户权限。

日期验证：确保工具在指定日期范围内使用。

要求
Python 3.x

ezdxf库

cryptography库

configparser库

安装
克隆仓库：

git https://github.com/shaoyi1998/CadTable2CSV.git
cd CadTable2CSV
安装所需的库：

pip install ezdxf cryptography configparser
使用
运行脚本：

python cad.py
确保在脚本所在目录中有DXF文件。

脚本将处理DXF文件并生成包含提取文本数据的CSV文件。

联系
如有任何疑问，请联系开发者 11711153217@qq.com。


This tool is designed to process DXF files and extract text data from ACAD_TABLE entities. It also includes functionality to manage user authentication using encrypted MAC addresses.

Features
DXF Processing: Extracts text data from ACAD_TABLE entities in DXF files and saves them as CSV files.

User Authentication: Uses encrypted MAC addresses to verify user permissions.

Date Validation: Ensures the tool is used within a specified date range.

Requirements
Python 3.x

ezdxf library

cryptography library

configparser library

Installation
Clone the repository:

git clone https://github.com/shaoyi1998/CadTable2CSV.git
cd CadTable2CSV
Install the required libraries:

pip install ezdxf cryptography configparser
Usage
Run the script:

python cad.py
Ensure you have DXF files in the same directory as the script.

The script will process the DXF files and generate CSV files with the extracted text data.

Contact
For any inquiries, please contact the developer at 11711153217@qq.com.
