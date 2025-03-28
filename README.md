# CTkDatePicker

CTkDatePicker is a custom date picker widget built using the CustomTkinter library. It provides a user-friendly interface for selecting dates, with both a text entry and a calendar popup for easy date selection.

![grafik](https://github.com/user-attachments/assets/d51430c3-aea1-49bf-b790-550c58902773)


## Features

- **Customizable Date Format**: Set the date format to display in the date entry.
- **Calendar Popup**: Provides a visual calendar for selecting dates.
- **Manual Date Entry**: Optionally allow users to manually enter a date.
- **Previous and Next Month Navigation**: Easily navigate between months.

## Installation

To use CTkDatePicker, you need to have CustomTkinter installed. You can install it using pip:

```bash
pip install customtkinter
```

## Usage

### Basic Example

Here's a basic example of how to use CTkDatePicker in your application:

```python
import tkinter as tk
import customtkinter as ctk
from CTkDatePicker import CTkDatePicker

def main():
    root = ctk.CTk()
    root.geometry("400x300")
    
    date_picker = CTkDatePicker(root)
    date_picker.set_allow_change_month(False)
    date_picker.set_change_months("sub", 5)
    date_picker.pack(pady=20)

    def print_date():
        print(f"Selected Date: {date_picker.get_date()}")

    btn = ctk.CTkButton(root, text="Print Date", command=print_date)
    btn.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()
```

### Customization

- **Date Format**: You can set the date format using the `set_date_format` method.

  ```python
  date_picker.set_date_format("%d-%m-%Y")
  ```

- **Language**: You can set the language for days and months using the `set_localization` method.

  ```python
  date_picker.set_localization("en_EN")
  ```

- **Allow Manual Input**: Enable or disable manual date input using the `set_allow_manual_input` method.

  ```python
  date_picker.set_allow_manual_input(True)  # Enable
  date_picker.set_allow_manual_input(False) # Disable
  ```

## Methods

### `set_date_format(date_format)`

- **Description**: Set the date format to be used in the date entry.
- **Parameters**: 
  - `date_format` (str): The desired date format string, e.g., "%m/%d/%Y".

### `set_localization(localization)`

- **Description**: Set the localization for month and day names.
- **Parameters**: 
  - `localization` (str): The desired localization string, e.g., "en_EN".

### `open_calendar()`

- **Description**: Open the calendar popup for date selection.

### `build_calendar()`

- **Description**: Build and display the calendar in the popup.

### `prev_month()`

- **Description**: Navigate to the previous month in the calendar.

### `next_month()`

- **Description**: Navigate to the next month in the calendar.

### `select_date(day)`

- **Description**: Select a date from the calendar.
- **Parameters**: 
  - `day` (int): The day of the month selected by the user.

### `get_date()`

- **Description**: Get the currently selected date as a string.
- **Returns**: 
  - `str`: The date string in the format specified by `self.date_format`.

### `set_allow_manual_input(value)`

- **Description**: Enable or disable manual date input.
- **Parameters**: 
  - `value` (bool): If True, manual input in the date entry is allowed; otherwise, it is disabled.

### `set_allow_change_month(value)`

- **Description**: Enable or disable change month.
- **Parameters**: 
  - `value` (bool): If False, user cannot change month in the calendar.

### `set_change_months(value)`

- **Description**: Add or subract number of months when opening the calendar.
- **Parameters**: 
  - `add_or_sub` (str): Either "add" or "sub".
  - `value` (int): Number of months.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for providing a great framework for creating modern and customizable GUI applications in Python.

Feel free to customize this README to better suit your project's specific details and needs!
