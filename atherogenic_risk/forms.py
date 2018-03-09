from wtforms import Form, FloatField, validators


class PrimaryForm(Form):
    total_cholesterol = FloatField(validators=[validators.required])
    triglyceride = FloatField(validators=[validators.required])
    high_density_lipoproteins = FloatField(validators=[validators.required])

    @property
    def very_low_density_lipoproteins(self):
        return self.triglyceride.data / 2.2

    @property
    def low_density_lipoproteins(self):
        raise NotImplementedError

    @property
    def atherosclerosis_index(self):
        return self.low_density_lipoproteins / self.high_density_lipoproteins





