"""
Safe string
"""

import re
from datetime import date

from unidecode import unidecode

CURP_REGEXP = r"^[A-Z]{4}\d{6}[A-Z]{6}[A-Z0-9]{2}$"
EMAIL_REGEXP = r"^[\w.-]+@[\w.-]+\.\w+$"
PASSWORD_REGEXP = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,24}$"
TELEFONO_REGEXP = r"^[1-9]\d{9}$"


def safe_clave(input_str, max_len=16, only_digits=False, separator="-") -> str:
    """Safe clave"""
    if not isinstance(input_str, str):
        return ""
    stripped = input_str.strip()
    if stripped == "":
        return ""
    if only_digits:
        clean_string = re.sub(r"[^0-9]+", separator, stripped)
    else:
        clean_string = re.sub(r"[^a-zA-Z0-9]+", separator, unidecode(stripped))
    without_spaces = re.sub(r"\s+", "", clean_string)
    final = without_spaces.upper()
    if len(final) > max_len:
        return final[:max_len]
    return final


def safe_curp(input_str, is_optional=False, search_fragment=False) -> str:
    """Safe CURP"""
    if not isinstance(input_str, str):
        return ""
    stripped = input_str.strip()
    if is_optional and stripped == "":
        return ""
    clean_string = re.sub(r"[^a-zA-Z0-9]+", " ", unidecode(stripped))
    without_spaces = re.sub(r"\s+", "", clean_string)
    final = without_spaces.upper()
    if search_fragment is False and re.match(CURP_REGEXP, final) is None:
        raise ValueError("CURP inválida")
    return final


def safe_email(input_str, search_fragment=False) -> str:
    """Safe email"""
    if not isinstance(input_str, str):
        return ""
    final = input_str.strip().lower()
    if search_fragment:
        if re.match(r"^[\w.-]*@*[\w.-]*\.*\w*$", final) is None:
            return ""
        return final
    if re.match(EMAIL_REGEXP, final) is None:
        raise ValueError("E-mail inválido")
    return final


def safe_expediente(input_str):
    """Safe expediente como 123/2023, 123/2023-II, 123/2023-II-2, 123/2023-F2"""
    if not isinstance(input_str, str) or input_str.strip() == "":
        return ""
    elementos = re.sub(r"[^a-zA-Z0-9]+", "|", unidecode(input_str.strip())).split("|")
    try:
        numero = int(elementos[0])
        ano = int(elementos[1])
    except (IndexError, ValueError) as error:
        raise error
    if ano < 1900 or ano > date.today().year:
        raise ValueError
    extra_1 = ""
    if len(elementos) >= 3:
        extra_1 = "-" + elementos[2].upper()
    extra_2 = ""
    if len(elementos) >= 4:
        extra_2 = "-" + elementos[3].upper()
    limpio = f"{str(numero)}/{str(ano)}{extra_1}{extra_2}"
    if len(limpio) > 16:
        raise ValueError
    return limpio


def safe_string(input_str, max_len=250, do_unidecode=True, save_enie=False, to_uppercase=True) -> str:
    """Safe string"""
    if not isinstance(input_str, str):
        return ""
    if do_unidecode:
        new_string = re.sub(r"[^a-zA-Z0-9.()/-]+", " ", input_str)
        if save_enie:
            new_string = ""
            for char in input_str:
                if char == "ñ":
                    new_string += "ñ"
                elif char == "Ñ":
                    new_string += "Ñ"
                else:
                    new_string += unidecode(char)
        else:
            new_string = re.sub(r"[^a-zA-Z0-9.()/-]+", " ", unidecode(input_str))
    else:
        if save_enie is False:
            new_string = re.sub(r"[^a-záéíóúüA-ZÁÉÍÓÚÜ0-9.()/-]+", " ", input_str)
        else:
            new_string = re.sub(r"[^a-záéíóúüñA-ZÁÉÍÓÚÜÑ0-9.()/-]+", " ", input_str)
    removed_multiple_spaces = re.sub(r"\s+", " ", new_string)
    final = removed_multiple_spaces.strip()
    if to_uppercase:
        final = final.upper()
    if max_len == 0:
        return final
    return (final[:max_len] + "…") if len(final) > max_len else final
