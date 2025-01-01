from django.shortcuts import render


def convert_length(value, from_unit, to_unit):
    length_units = {
        'mm': 1, 'cm': 10, 'm': 1000, 'km': 1000000,
        'in': 25.4, 'ft': 304.8, 'yd': 914.4, 'mi': 1609344
    }
    value_in_mm = value * length_units[from_unit]  
    return value_in_mm / length_units[to_unit]


def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'mg': 1, 'g': 1000, 'kg': 1000000, 'oz': 28349.5, 'lb': 453592
    }
    value_in_mg = value * weight_units[from_unit]  # Convert to milligrams first
    return value_in_mg / weight_units[to_unit]

# Temperature Conversion Functions
def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    return value

# Main view to handle form and conversion
def index(request):
    result = None
    category = None  # Initialize category with a default value
    if request.method == 'POST':
        category = request.POST.get('category', '')  # Get the category from POST data
        if 'value' not in request.POST:
            result = "Value field is missing!"
        else:
            try:
                value = float(request.POST['value'])
                from_unit = request.POST['from_unit']
                to_unit = request.POST['to_unit']
                if category == 'length':
                    result = convert_length(value, from_unit, to_unit)
                elif category == 'weight':
                    result = convert_weight(value, from_unit, to_unit)
                elif category == 'temperature':
                    result = convert_temperature(value, from_unit, to_unit)
            except Exception as e:
                result = f"Error: {str(e)}"
    # Render the page with the category, result, and form
    return render(request, 'index.html', {'result': result, 'category': category})
