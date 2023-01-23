import { required, minLength, minValue, email } from "vuelidate/lib/validators";


//HES Code checking algorithm for validation
function hesCheck(val) {
  let reg = /^[A-Z][0-9][A-Z][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9]$/g;
  return reg.test(val);
}

//Phone format checking algorithm (format => 5557778899)
function phoneCheck(val) {
  let reg = /^\d{10}$/;
  if (val === "") return true;
  else return reg.test(val);
}

export const FormValidation = {
  validations: {
    fname: {
      required,
      minLength: minLength(3),
    },
    lname: {
      required,
      minLength: minLength(3),
    },
    age: {
      required,
      minValue: minValue(6),
    },
    email: {
      required,
      email,
    },
    sex: {
      required,
    },
    hes: {
      required,
      hesCheck,
    },
    phone: {
      required,
      phoneCheck,
    },
  },
};
